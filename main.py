import json
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch


class EthicsAssistant:
    def __init__(self, model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0"):
        self.model_name = model_name
        self.knowledge_base = self.load_knowledge_base('ethics_rules.json')

        print(f"Загрузка модели {model_name}...")
        print("(Это может занять несколько минут при первом запуске)")

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            trust_remote_code=True
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto",
            low_cpu_mem_usage=True,
            trust_remote_code=True
        )

        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device_map="auto"
        )

        print("Модель успешно загружена и готова к работе!")

    def load_knowledge_base(self, file_path: str) -> list:
        """Загружаем базу знаний с правилами этикета"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Файл {file_path} не найден!")
            return []

    def find_relevant_rule(self, user_question: str) -> str:
        """Умный поиск по ключевым словам"""
        user_question_lower = user_question.lower()
        for entry in self.knowledge_base:
            topic = entry['topic'].lower()

            if topic == 'знакомство':
                keywords = ['знакомств', 'предста', 'руку', 'подать', 'познаком', 'представ']
            elif topic == 'переписка':
                keywords = ['переписк', 'письм', 'email', 'сообщен', 'капс', 'caps', 'мессенджер', 'whatsapp', 'телеграм']
            elif topic == 'звонок':
                keywords = ['звонок', 'позвонить', 'телефон', 'звонить', 'поздрав', 'созвонить']
            elif topic == 'соцсети':
                keywords = ['соцсет', 'социальн', 'instagram', 'инстаграм', 'facebook', 'фейсбук', 'вконтакте', 'vk', 'twitter', 'твиттер', 'фото', 'photograph', 'публикац']
            elif topic == 'разговор':
                keywords = ['разговор', 'бесед', 'общен', 'слуша', 'перебив', 'диалог', 'обсужден']
            elif topic == 'гости':
                keywords = ['гост', 'визит', 'приход', 'подарок', 'цветы', 'десерт', 'приглашен', 'хозяйк']
            else:
                keywords = [topic]

            if any(keyword in user_question_lower for keyword in keywords):
                return entry['rule']

        return None

    def generate_response(self, user_question: str) -> str:
        """Генерация ответа с использованием модели"""
        relevant_rule = self.find_relevant_rule(user_question)

        if not relevant_rule:
            return "Извините, в моей базе знаний нет информации по этому вопросу."

        if "TinyLlama" in self.model_name:
            prompt = f"""<|system|>
            Ты ассистент по этикету. Отвечай ТОЛЬКО на основе предоставленного правила.
            Не добавляй ничего от себя. Отвечай кратко и по делу.</s>
            <|user|>
            ПРАВИЛО: {relevant_rule}
            ВОПРОС: {user_question}
            ОТВЕТАЙ ТОЛЬКО НА ОСНОВЕ ПРАВИЛА ВЫШЕ.</s>
            <|assistant|>
            На основе правила:"""
        else:
            # Универсальный промпт для других моделей
            prompt = f"""Ты консультант по этикету. Ответь на вопрос строго на основе предоставленного правила.
            Не придумывай ничего от себя. Будь точным и лаконичным.

            Правило: {relevant_rule}
            Вопрос: {user_question}

            Ответ:"""

        try:
            outputs = self.pipe(
                prompt,
                max_new_tokens=150,
                do_sample=True,
                temperature=0.3,
                top_p=0.9,
                pad_token_id=self.tokenizer.eos_token_id
            )

            full_response = outputs[0]['generated_text']
            response = full_response.replace(prompt, "").strip()
            return response

        except Exception as e:
            return f"Произошла ошибка: {str(e)}"


def main():
    # Инициализируем ассистента с открытой моделью
    assistant = EthicsAssistant("TinyLlama/TinyLlama-1.1B-Chat-v1.0")

    print("\n🤵 Этикет-консультант готов к работе!")
    print("Задайте вопрос по этикету (или 'выход' для завершения):")

    while True:
        user_input = input("\nВаш вопрос: ").strip()

        if user_input.lower() in ['выход', 'exit', 'quit']:
            print("До свидания!")
            break

        if not user_input:
            continue

        response = assistant.generate_response(user_input)
        print(f"\nОтвет: {response}")


if __name__ == "__main__":
    main()
