import os
from typing import List, Optional
from loguru import logger
from docx import Document
import pytesseract
from pdf2image import convert_from_path


class DocumentProcessor:
    def __init__(self):
        logger.info("Инициализация Document Processor")
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def extract_text(self, file_path: str) -> Optional[str]:
        """Основной метод извлечения текста из файла"""
        filename = file_path.lower()

        try:
            if filename.endswith('.pdf'):
                return self.extract_text_from_pdf(file_path)
            elif filename.endswith('.docx'):
                return self.extract_text_from_docx(file_path)
            elif filename.endswith('.txt'):
                return self.extract_text_from_txt(file_path)
            else:
                logger.warning(f"Неподдерживаемый формат: {file_path}")
                return None

        except Exception as e:
            logger.error(f"Ошибка извлечения текста из {file_path}: {e}")
            return None

    def extract_text_from_pdf(self, file_path: str) -> str:
        """Извлечение текста из PDF с использованием pypdf"""
        try:
            from pypdf import PdfReader
            text = ""
            with open(file_path, 'rb') as file:
                reader = PdfReader(file)
                for page_num, page in enumerate(reader.pages):
                    try:
                        page_text = page.extract_text()
                        if page_text:
                            text += f"\n--- Страница {page_num + 1} ---\n{page_text}"
                    except Exception as page_error:
                        logger.warning(f"Ошибка страницы {page_num + 1}: {page_error}")
                        continue

            return text.strip()
        except Exception as e:
            logger.error(f"Ошибка pypdf для {file_path}: {e}")
            return ""

    def _extract_text_with_ocr(self, file_path: str) -> str:
        """Извлечение текста из PDF с помощью OCR"""
        try:
            text = ""
            # Конвертируем PDF в изображения
            images = convert_from_path(file_path, dpi=200)

            for i, image in enumerate(images):
                # Увеличиваем контраст для лучшего распознавания
                image = image.convert('L')  # Grayscale

                # Распознаем текст
                page_text = pytesseract.image_to_string(image, lang='rus+eng')
                text += f"\n--- Страница {i+1} ---\n{page_text}"

            return text.strip()

        except Exception as e:
            logger.error(f"Ошибка OCR для {file_path}: {e}")
            return ""

    def extract_text_from_docx(self, file_path: str) -> str:
        """Извлечение текста из DOCX"""
        try:
            doc = Document(file_path)
            full_text = []

            # Текст из параграфов
            for paragraph in doc.paragraphs:
                if paragraph.text.strip():
                    full_text.append(paragraph.text)

            # Текст из таблиц
            for table in doc.tables:
                for row in table.rows:
                    for cell in row.cells:
                        if cell.text.strip():
                            full_text.append(cell.text)

            return '\n'.join(full_text)

        except Exception as e:
            logger.error(f"Ошибка чтения DOCX {file_path}: {e}")
            return ""

    def extract_text_from_txt(self, file_path: str) -> str:
        """Извлечение текста из TXT"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            # Пробуем другие кодировки
            try:
                with open(file_path, 'r', encoding='cp1251') as f:
                    return f.read()
            except Exception as e:
                logger.error(f"Ошибка чтения TXT {file_path}: {e}")
                return ""
        except Exception as e:
            logger.error(f"Ошибка чтения TXT {file_path}: {e}")
            return ""

    def chunk_text(self, text: str,
                   chunk_size: int = 500,
                   overlap: int = 50) -> List[str]:
        """Разбивка текста на перекрывающиеся чанки"""
        if not text or chunk_size <= 0:
            return []

        words = text.split()

        if len(words) <= chunk_size:
            return [' '.join(words)]

        chunks = []
        i = 0

        while i < len(words):
            chunk = ' '.join(words[i:i + chunk_size])
            chunks.append(chunk)

            # Сдвигаемся с перекрытием
            i += chunk_size - overlap

            # Если осталось меньше chunk_size слов, берем остаток и выходим
            if i + chunk_size >= len(words):
                remaining_chunk = ' '.join(words[i:])
                if remaining_chunk.strip():
                    chunks.append(remaining_chunk)
                break

        logger.debug(f"Текст разбит на {len(chunks)} чанков")
        return chunks

    def get_document_info(self, file_path: str) -> dict:
        """Получение информации о документе"""
        try:
            stat = os.stat(file_path)
            text = self.extract_text(file_path)

            return {
                "filename": os.path.basename(file_path),
                "size_bytes": stat.st_size,
                "char_count": len(text) if text else 0,
                "word_count": len(text.split()) if text else 0,
                "file_type": os.path.splitext(file_path)[1].lower()
            }
        except Exception as e:
            logger.error(f"Ошибка получения информации о документе {file_path}: {e}")
            return {}
