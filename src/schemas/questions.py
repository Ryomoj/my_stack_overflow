from pydantic import BaseModel


class QuestionAddSchema(BaseModel):
    text: str


class QuestionSchema(QuestionAddSchema):
    id: int
