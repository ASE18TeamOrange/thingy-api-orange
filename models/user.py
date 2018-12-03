from aiohttp.web import Response, View, json_response
from aiohttp_cors import CorsViewMixin
from models.database import Database

from models import user
from uuid import uuid4
from datetime import datetime
import json
from ast import literal_eval


class User:
    @classmethod
    async def create(cls, login, password):
        redis = Database()
        llogin = login.lower()

        if redis.get_hash('users:', llogin):
            # print(redis.get_hash('users:', llogin))
            print("User with login %s already exists" % llogin)
            return None

        # We also store a HASH of lowercased login names to user IDs, so if there’s already a login name that maps to an ID, we know and won’t give it to a second person.
        
        uuid = str(uuid4())

        credentials = {
            "id" : uuid,
            "passwd" : password
        }

        redis.set_hash('users:', llogin, credentials)

        # Add the lowercased login name to the HASH that maps from login names to user IDs.

        redis.set_hash_multiple("user:%s"%uuid, {
            "login" : login,
            "id" : uuid,
            "thingy" : "",
            "sensors" : []
        })
        
        return uuid

    @classmethod
    async def delete(cls, login):
        redis = Database()
        llogin = login.lower()

        db_entry = redis.get_hash('users:', llogin)
        print("ed", db_entry)

        if db_entry is None:
            return None
        else:
            user_dict = literal_eval(db_entry.decode('utf-8'))
            print(user_dict)
            uuid = user_dict['id']
            print("user:%s"%uuid)
            redis.delete("user:%s"%uuid)
            return redis.delete_hash("users:", login)


# class User:

#     async def create(self, name, pwd):
#         redis = Database()
#         if not self.exists(name, pwd):
#             redis.insert(name, pwd)
#             return True
#         return False

#     async def delete(self, name, pwd):
#         redis = Database()
#         if self.exists(name, pwd):
#             redis.delete(name)
#             return True
#         return False

#     async def exists(self, name, pwd):
#         redis = Database()
#         user = redis.get(name)
#         if user is not None:
#             return user.pwd == pwd
#         return False
