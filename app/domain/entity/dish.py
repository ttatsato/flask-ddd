from app.domain.value_object.cuisine import Cuisine


class Dish:
    def __init__(self, id: int, name: str, cuisine: str) -> None:
        self.id: int = id
        self.name: str = name
        self.cuisine: Cuisine = Cuisine(cuisine)

    def to_dict(self):
        return dict(
            dish_id=self.id,
            name=self.name,
            cuisine=dict(
                value=self.cuisine.value,
                label=self.cuisine.to_label()
            )
        )
