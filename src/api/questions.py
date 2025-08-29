from datetime import datetime

from fastapi import APIRouter

from src.api.dependencies import DatabaseDep
from src.schemas.questions import QuestionAddSchema

router = APIRouter(prefix="/questions", tags=["Вопросы"])


@router.get("/", summary="Получение списка всех вопросов")
async def get_all_questions(db: DatabaseDep):
    return await db.questions.get_all()


@router.post("/", summary="Создание нового вопроса")
async def create_new_question(db: DatabaseDep, question_data: QuestionAddSchema):
    question = await db.questions.add(question_data, created_at=datetime.now())
    await db.commit()
    return {"Status": "OK", "question": question}


@router.get("/{id}", summary="Получение конкретного вопроса с ответами по ID")
async def get_question_by_id(db: DatabaseDep, question_id: int):
    return await db.questions.get_one_or_none(id=question_id)


@router.delete("/{id}", summary="Удаление вопроса по ID")
async def delete_question_by_id(db: DatabaseDep, question_id: int):
    await db.questions.delete(id=question_id)
    await db.commit()
    return {"Status": "OK"}
