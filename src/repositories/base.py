import logging
from typing import Any

from asyncpg import UniqueViolationError
from pydantic import BaseModel
from sqlalchemy import select, insert, delete
from sqlalchemy.exc import IntegrityError

from src.exceptions.exceptions import ObjectAlreadyExistsException
from src.repositories.mappers.base import DataMapper


class BaseRepository:
    model = None
    mapper: DataMapper = None

    def __init__(self, session):
        self.session = session

    async def get_all(self):
        query = select(self.model)
        result = await self.session.execute(query)
        return [self.mapper.map_to_domain_entity(model) for model in result.scalars().all()]

    async def get_one_or_none(self, **kwargs):
        query = select(self.model).filter_by(**kwargs)
        result = await self.session.execute(query)
        model = result.scalars().one_or_none()
        if model is None:
            return None
        return self.mapper.map_to_domain_entity(model)

    async def add(self, data: BaseModel, **kwargs) -> BaseModel | Any:
        try:
            add_data_stmt = (
                insert(self.model).values(**data.model_dump(), **kwargs).returning(self.model)
            )
            result = await self.session.execute(add_data_stmt)
            model = result.scalars().one()
            return self.mapper.map_to_domain_entity(model)
        except IntegrityError as exc:
            logging.error(
                f"Не удалось добавить данные в БД, входные данные={data} тип ошибки: {type(exc.orig.__cause__)=}"
            )
            if isinstance(exc.orig.__cause__, UniqueViolationError):
                raise ObjectAlreadyExistsException from exc
            else:
                logging.error(
                    f"Незнакомая ошибка, Не удалось добавить данные в БД, входные данные={data} тип ошибки: {type(exc.orig.__cause__)=}"
                )
                raise exc

    async def delete(self, **kwargs) -> None:
        delete_stmt = delete(self.model).filter_by(**kwargs)
        await self.session.execute(delete_stmt)
