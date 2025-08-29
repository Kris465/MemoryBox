import os
import asyncio
import json
import numpy as np
from sentence_transformers import SentenceTransformer, util
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()


class EthicsAssistant:
    def __init__(self):
        # Загружаем маленькую модель для эмбеддингов (векторных представлений)
        print("Загрузка модели для распознавания...")
        self.embedding_model = SentenceTransformer(
            'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
        self.knowledge_base = self.load_knowledge_base('ethics_rules.json')
        self.setup_knowledge_embeddings()
        print("Модель для распознавания загружена!")

    def load_knowledge_base(self, file_path: str) -> list:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Файл {file_path} не найден!")
            return []

    def setup_knowledge_embeddings(self):
        """Создаем векторные представления для всех правил"""
        self.rules_texts = []
        self.rules_embeddings = []

        for entry in self.knowledge_base:
            rule_variants = [
                entry['topic'],
                f"правила {entry['topic']}",
                f"этикет {entry['topic']}",
                f"как вести себя {entry['topic']}",
                entry['rule'][:100]
            ]

            for variant in rule_variants:
                self.rules_texts.append({
                    'topic': entry['topic'],
                    'rule': entry['rule'],
                    'variant': variant
                })

        if self.rules_texts:
            texts_to_embed = [item['variant'] for item in self.rules_texts]
            self.rules_embeddings = self.embedding_model.encode(
                texts_to_embed, convert_to_tensor=True)

    def find_relevant_rule_semantic(self, user_question: str) -> str:
        """Поиск правила с использованием семантического similarity"""
        if not self.rules_texts:
            return None

        question_embedding = self.embedding_model.encode(
            user_question, convert_to_tensor=True)

        cos_scores = util.cos_sim(question_embedding, self.rules_embeddings)[0]

        best_match_idx = np.argmax(cos_scores.cpu().numpy())
        best_score = cos_scores[best_match_idx].item()

        if best_score > 0.3:
            best_match = self.rules_texts[best_match_idx]
            return best_match['rule']

        return None

    def find_relevant_rule_hybrid(self, user_question: str) -> str:
        """Гибридный поиск: сначала семантический, потом по ключевым словам"""
        rule = self.find_relevant_rule_semantic(user_question)
        if rule:
            return rule

        user_question_lower = user_question.lower()
        for entry in self.knowledge_base:
            topic = entry['topic'].lower()

            if topic == 'знакомство':
                keywords = ['знакомств', 'предста', 'руку', 'подать',
                            'познаком']
            elif topic == 'переписка':
                keywords = ['переписк', 'письм', 'email', 'сообщен', 'капс',
                            'caps']
            elif topic == 'звонок':
                keywords = ['звонок', 'позвонить', 'телефон', 'звонить']
            elif topic == 'соцсети':
                keywords = ['соцсет', 'социальн', 'instagram', 'инстаграм',
                            'фото']
            elif topic == 'разговор':
                keywords = ['разговор', 'бесед', 'общен', 'слуша', 'перебив']
            elif topic == 'гости':
                keywords = ['гост', 'визит', 'приход', 'подарок', 'цветы']
            else:
                keywords = [topic]

            if any(keyword in user_question_lower for keyword in keywords):
                return entry['rule']

        return None

    def generate_response(self, user_question: str) -> str:
        """Просто возвращаем найденное правило без генерации"""
        relevant_rule = self.find_relevant_rule_hybrid(user_question)

        if not relevant_rule:
            return "Извините, в моей базе знаний нет информации по этому вопросу. Попробуйте задать вопрос по-другому."

        return f"📖 Правило этикета:\n\n{relevant_rule}"


assistant = EthicsAssistant()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message):
    welcome_text = """
    🤵 Этикет-Консультант приветствует вас!

    Я помогу вам с правилами этикета:
    • Знакомство и представление
    • Деловая переписка  
    • Телефонные звонки
    • Поведение в соцсетях
    • Культура общения
    • Прием гостей

    Просто задайте вопрос, например:
    "Как вести себя при знакомстве?"
    "Что нельзя делать в переписке?"
    "Как правильно звонить?"
    "Как вести себя в соцсетях?"
    """
    await message.answer(welcome_text)


@dp.message(Command("help"))
async def cmd_help(message: Message):
    help_text = """
    Помощь по боту:

    Доступные команды:
    /start - начать работу
    /help - показать справку
    /topics - показать темы

    Напишите вопрос о правилах этикета!
    """
    await message.answer(help_text)


@dp.message(Command("topics"))
async def cmd_topics(message: Message):
    topics = []
    for entry in assistant.knowledge_base:
        topics.append(f"• {entry['topic'].capitalize()}")

    topics_text = "📚 Доступные темы:\n\n" + "\n".join(topics)
    await message.answer(topics_text)


@dp.message(F.text)
async def handle_message(message: Message):
    user_question = message.text.strip()

    if len(user_question) < 3 or user_question.startswith('/'):
        return

    await message.bot.send_chat_action(message.chat.id, "typing")
    await asyncio.sleep(0.5)

    response = assistant.generate_response(user_question)
    await message.answer(response)


async def main():
    print("Бот запускается...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
