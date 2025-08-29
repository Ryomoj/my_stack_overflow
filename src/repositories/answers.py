from src.models.answers import AnswersOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import AnswersDataMapper


class AnswersRepository(BaseRepository):
    model = AnswersOrm
    mapper = AnswersDataMapper
