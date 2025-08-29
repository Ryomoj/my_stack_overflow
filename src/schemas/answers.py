from pydantic import BaseModel


class AnswerAddSchema(BaseModel):
    text: str


class AnswerSchema(AnswerAddSchema):
    id: int
