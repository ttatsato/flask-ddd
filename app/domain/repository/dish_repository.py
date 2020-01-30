from app.domain.entity.dish import Dish
from conf.database import Database


class DishRepository:
    fields: list = ['id', 'name', 'cuisine']

    @classmethod
    def find(cls, conditions: dict={}) -> list:
        db = Database.connect_db()
        if db:
            query = 'SELECT id, name, cuisine FROM dish {where}'
            where = ""
            if conditions:
                c_list = ["{}={}".format(*k_v) for k_v in conditions.items()]
                c_str = " AND".join(c_list)
                where = "WHERE {conditions}".format(conditions=c_str)

            db.execute(query.format(where=where))
            return db.fetchall()
        else:
            return []

    @classmethod
    def find_with_dishes(cls, conditions: dict={}) -> list:
        rows = cls.find(conditions)
        return [Dish(**val) for val in rows]