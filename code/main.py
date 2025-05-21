from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn
import datetime
import json
from pathlib import Path

app = FastAPI()

# Разрешаем CORS, чтобы фронтенд на localhost:xxxx мог обращаться к бэкенду
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Файл для хранения отзывов
REVIEWS_FILE = Path("reviews.json")


# Модель входящих данных
class ReviewInput(BaseModel):
    review: str


# Модель хранения с датой
class Review(ReviewInput):
    created_at: datetime.datetime


# Загрузка отзывов из JSON
def load_reviews() -> List[Review]:
    if REVIEWS_FILE.exists():
        with REVIEWS_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return [Review(**item) for item in data]
    return []


# Сохранение отзывов в JSON
def save_reviews(reviews: List[Review]):
    with REVIEWS_FILE.open("w", encoding="utf-8") as f:
        json.dump([review.dict() for review in reviews], f, ensure_ascii=False, indent=2, default=str)


@app.post("/reviews")
async def add_review(review: ReviewInput):
    reviews = load_reviews()
    new_review = Review(review=review.review, created_at=datetime.datetime.now())
    reviews.append(new_review)
    save_reviews(reviews)

    print(f"Добавлен отзыв: \"{review.review}\" отправлен {new_review.created_at.strftime('%H:%M:%S %d.%m.%Y')}")
    return {"message": "Отзыв добавлен", "review": review.review}


@app.get("/reviews")
async def get_reviews():
    reviews = load_reviews()
    return {"reviews": reviews}

uvicorn.run(app, host="0.0.0.0", port=8000)
