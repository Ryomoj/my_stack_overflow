class BookingsException(Exception):
    detail = "Неожиданная ошибка"

    def __init__(self, *args, **kwargs):
        super().__init__(self.detail, *args, **kwargs)


class ObjectAlreadyExistsException(BookingsException):
    detail = "Объект уже существует"
