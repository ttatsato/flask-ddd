from app.infrastructure.repository.mysql.datamodel.models import session, Dish


class DishRepository:
    fields: list = ['id', 'name', 'cuisine']

    @classmethod
    def find(cls) -> list:
        return session.query(Dish).all()