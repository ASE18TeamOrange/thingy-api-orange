import redis
import math


class Database:
    """
    Database handler for Redis db.
    Implements functions for operating on Redis sorted sets (ZSET).
    """

    __connection = None

    def __init__(self):
        self.__connection = redis.Redis(host='localhost', port=6379, db=0)

    def enqueue(self, key, value, score):
        self.__connection.zadd(key, value, score)

    def insert(self, key, value):
        self.__connection.set(key, value)

    def get(self, key):
        return self.__connection.get(key)

    def exists(self, key):
        return self.__connection.exists(key)

    def get_set(self, key, start, end):
        return self.__connection.zrange(key, start, end)

    def get_set_len(self, key):
        return len(self.__connection.zrange(key, 0, -1))

    def delete(self, key):
        self.__connection.delete(key)
