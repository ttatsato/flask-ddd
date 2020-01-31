from app.domain.entity.dish import DishEntity
from app.domain.value_object.cuisine import Cuisine
from app.infrastructure.repository.mysql.repository.dish_repository import DishRepository


class DishService:

    @classmethod
    def find_with_dishes(cls) -> list:
        rows: list = DishRepository.find()
        if rows:
            return [DishEntity(id=val.id, name=val.name, cuisine=Cuisine.Western) for val in rows]
        else:
            return []