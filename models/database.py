import redis


class Database:

    __connection = None

    def __init__(self):
        self.__connection = redis.Redis(host='localhost', port=6379, db=0)

    def enqueue(self, key, value):
        self.__connection.rpush(key, value)

    def insert(self, key, value):
        self.__connection.set(key, value)

    def get(self, key):
        return self.__connection.get(key)

    def getList(self, key, start, end):
        return self.__connection.lrange(key, start, end)

    def getListLength(self, key):
        return self.__connection.llen(key)

    def delete(self, key):
        self.__connection.delete(key)
