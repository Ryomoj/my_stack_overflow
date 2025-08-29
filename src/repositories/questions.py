from src.models.questions import QuestionsOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import QuestionsDataMapper


class QuestionsRepository(BaseRepository):
    model = QuestionsOrm
    mapper = QuestionsDataMapper
