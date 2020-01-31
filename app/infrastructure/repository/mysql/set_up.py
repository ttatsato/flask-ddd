import mysql.connector as connector
import os


class Database:

    @classmethod
    def connect_db(cls) -> connector.connection:
        try:
            connect = connector.connect(
                user=os.getenv('MYSQL_USER'),
                password=os.getenv('MYSQL_ROOT_PASSWORD'),
                host=os.getenv('MYSQL_CONTAINER_NAME'),
                database=os.getenv('MYSQL_DATABASE'),
                charset='utf8'
            )
            return connect.cursor(dictionary=True)
        except connector.Error:
            print("connection Error")
            return None