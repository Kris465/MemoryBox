import os
from loguru import logger
import chromadb
from sentence_transformers import SentenceTransformer

from models import DocumentChunk, SearchResult
from document_processor import DocumentProcessor


class VectorDatabase:
    def __init__(self, persist_directory: str = "./vector_db"):
        logger.info("Инициализация Vector Database")

        # Инициализация энкодера
        self.encoder = SentenceTransformer(
            'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'
        )

        # Инициализация процессора документов
        self.doc_processor = DocumentProcessor()

        # Инициализация ChromaDB
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(
            name="research_documents",
            metadata={"description": "База научных документов для Research Assistant"}
        )

        logger.info(f"Vector DB инициализирована. Коллекция: {self.collection.name}")

    def add_document(self, file_path: str) -> int:
        """Добавление документа в векторную БД"""
        try:
            filename = os.path.basename(file_path)
            logger.debug(f"Добавление документа: {filename}")

            # Извлекаем текст из документа
            text = self.doc_processor.extract_text(file_path)
            if not text:
                logger.warning(f"Не удалось извлечь текст из {filename}")
                return 0

            chunks = self.doc_processor.chunk_text(text,
                                                   chunk_size=500,
                                                   overlap=50)

            if not chunks:
                logger.warning(f"Не удалось разбить на чанки: {filename}")
                return 0

            # Создаем эмбеддинги для чанков
            embeddings = self.encoder.encode(chunks).tolist()

            # Подготавливаем метаданные и ID
            metadatas = [
                {
                    "source": filename,
                    "chunk_index": i,
                    "total_chunks": len(chunks),
                    "file_type": os.path.splitext(filename)[1].lower()
                }
                for i in range(len(chunks))
            ]

            ids = [f"{filename}_{i}" for i in range(len(chunks))]

            # Добавляем в коллекцию
            self.collection.add(
                embeddings=embeddings,
                documents=chunks,
                metadatas=metadatas,
                ids=ids
            )

            logger.info(f"✅ Добавлен {filename}: {len(chunks)} чанков")
            return len(chunks)

        except Exception as e:
            logger.error(f"❌ Ошибка добавления документа {file_path}: {e}")
            return 0

    def search(self, query: str, n_results: int = 5) -> SearchResult:
        """Поиск релевантных документов по запросу"""
        try:
            logger.debug(f"Поиск: '{query}' (n_results={n_results})")

            # Создаем эмбеддинг для запроса
            query_embedding = self.encoder.encode([query]).tolist()

            # Выполняем поиск
            results = self.collection.query(
                query_embeddings=query_embedding,
                n_results=n_results,
                include=["documents", "metadatas", "distances"]
            )

            # Преобразуем результаты в наши модели
            chunks = []
            for i, (doc, metadata, distance) in enumerate(zip(
                results['documents'][0],
                results['metadatas'][0],
                results['distances'][0]
            )):
                chunk = DocumentChunk(
                    text=doc,
                    source=metadata.get('source', 'unknown'),
                    page=metadata.get('page'),
                    metadata={
                        'chunk_index': metadata.get('chunk_index'),
                        'similarity_score': 1 - distance,  # Преобразуем расстояние в схожесть
                        'file_type': metadata.get('file_type')
                    }
                )
                chunks.append(chunk)

            search_result = SearchResult(
                chunks=chunks,
                query=query,
                total_found=len(chunks)
            )

            logger.debug(f"🔍 Найдено {len(chunks)} результатов для '{query}'")
            return search_result

        except Exception as e:
            logger.error(f"❌ Ошибка поиска: {e}")
            return SearchResult(chunks=[], query=query, total_found=0)

    def get_collection_stats(self) -> dict:
        """Получение статистики коллекции"""
        try:
            count = self.collection.count()
            return {
                "total_chunks": count,
                "collection_name": self.collection.name
            }
        except Exception as e:
            logger.error(f"Ошибка получения статистики: {e}")
            return {"total_chunks": 0, "collection_name": "error"}

    def clear_collection(self):
        """Очистка коллекции"""
        try:
            self.client.delete_collection(self.collection.name)
            self.collection = self.client.get_or_create_collection("research_documents")
            logger.info("✅ Коллекция очищена")
        except Exception as e:
            logger.error(f"❌ Ошибка очистки коллекции: {e}")

    def document_exists(self, file_path: str) -> bool:
        """Проверка, существует ли документ уже в БД"""
        try:
            filename = os.path.basename(file_path)
            # Ищем чанки с этим источником
            results = self.collection.get(
                where={"source": filename},
                limit=1
            )
            return len(results['ids']) > 0
        except Exception as e:
            logger.error(f"Ошибка проверки документа {file_path}: {e}")
            return False
