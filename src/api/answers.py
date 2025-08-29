from datetime import datetime

from fastapi import APIRouter

from src.api.dependencies import DatabaseDep
from src.schemas.answers import AnswerAddSchema
from src.utils.user_id_util import create_new_uuid

router = APIRouter(prefix="", tags=["Ответы"])


@router.post("/questions/{question_id}/answers", summary="Добавление нового ответа")
async def add_new_answer(db: DatabaseDep, answer_data: AnswerAddSchema, question_id: int):
    new_uuid = create_new_uuid()

    answer = await db.answers.add(
        answer_data,
        created_at=datetime.now(),
        user_id=new_uuid,
        question_id=question_id,
    )

    await db.commit()
    return {"Status": "OK", "answer": answer}


@router.get("/answers/{answer_id}", summary="Получение конкретного ответа по ID")
async def get_answer_by_id(db: DatabaseDep, answer_id: int):
    return await db.answers.get_one_or_none(id=answer_id)


@router.delete("/answers/{answer_id}", summary="Удаление ответа по ID")
async def delete_answer_by_id(db: DatabaseDep, answer_id: int):
    await db.answers.delete(id=answer_id)
    await db.commit()
    return {"Status": "OK"}
