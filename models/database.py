from redis import *


class Database:

    __database = None

    def __setup_database(self):
        if self.__database is None:
            __database = StrictRedis(host='localhost', port=6379, db=0)
        return __database

    def insert(self, key, value):
        if self.__database is None:
            self.__setup_database()
        self.__database.set(key, value)

    def get(self, key):
        if self.__database is None:
            self.__setup_database()
        return self.__database.get(key)

    def delete(self, key):
        if self.__database is None:
            self.__setup_database()
        self.__database.remove(key)
