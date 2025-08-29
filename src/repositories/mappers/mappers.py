from src.models.answers import AnswersOrm
from src.models.questions import QuestionsOrm
from src.repositories.mappers.base import DataMapper
from src.schemas.answers import AnswerSchema
from src.schemas.questions import QuestionSchema


class QuestionsDataMapper(DataMapper):
    db_model = QuestionsOrm
    schema = QuestionSchema


class AnswersDataMapper(DataMapper):
    db_model = AnswersOrm
    schema = AnswerSchema
