from aiohttp.web import Response, View, json_response
from aiohttp_cors import CorsViewMixin
from models.database import Database

from models import user
from uuid import uuid4
from datetime import datetime, timedelta
import json
from ast import literal_eval
import jwt


JWT_ALG = "HS256"


class User:
    @classmethod
    async def create(cls, login, password):
        redis = Database()
        llogin = login.lower()

        if redis.get_hash('users:', llogin):
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
        print(llogin)
        db_entry = redis.get_hash('users:', llogin)
        print("ed", db_entry)

        if db_entry is None:
            print('none')
            return None
        else:
            user_dict = literal_eval(db_entry.decode('utf-8'))
            print(user_dict)
            uuid = user_dict['id']
            print("user:%s"%uuid)
            redis.delete("user:%s"%uuid)
            return redis.delete_hash("users:", login)

    
    @classmethod
    async def login(cls, login, password, secret):
        redis = Database()
        llogin = login.lower()

        #if redis.get_hash('sessions:', llogin):
        #    print("User with login %s already logged in" % llogin)
        #    return None

        if redis.key_exists_in_hash('users:', llogin):
            login_entry = redis.get_hash('users:', llogin)
            login_dict = literal_eval(login_entry.decode('utf-8'))
            print(login_dict)
            db_password = login_dict['passwd']
            print(password)
            print(db_password)
            if password != db_password:
                return None
            else:
                uuid = login_dict['id']
                jwt_token = jwt.encode(
                    {
                        'uuid' : uuid,
                        'login' : login,
                        'exp' : datetime.utcnow() + timedelta(minutes=30)
                    }, secret, algorithm=JWT_ALG)
                str_token = jwt_token.decode('utf-8')

                content = {
                    "token" : str_token
                }

                redis.set_hash('sessions:', llogin, content)

                return json_response({"token" : str_token}, status=200)
        else:
            return None
    

    @classmethod
    async def logout(cls, login):
        redis = Database()
        llogin = login.lower()

        if redis.get_hash('sessions:', llogin):
            return redis.delete_hash('sessions:', llogin)
        
        return None


    @classmethod
    async def get_profile(cls, login):
        redis = Database()
        llogin = login.lower()

        if redis.key_exists_in_hash('users:', llogin):
            db_entry = redis.get_hash('users:', llogin)
            user_dict = literal_eval(db_entry.decode('utf-8'))
            uuid = user_dict['id']

            profile_before = redis.get_hash_all("user:%s"%uuid)

            profile = convert(profile_before)
            #profile['sensors'] = literal_eval(profile['sensors'])
            return profile
        
        return None
    

    @classmethod
    async def connect_thingy(cls, login, thingy):
        redis = Database()
        llogin = login.lower()

        if redis.key_exists_in_hash('users:', llogin):
            db_entry = redis.get_hash('users:', llogin)
            user_dict = literal_eval(db_entry.decode('utf-8'))
            uuid = user_dict['id']
            print(uuid)

            return redis.set_hash("user:%s"%uuid, "thingy", thingy)
        
        return None





def convert(data):
    if isinstance(data, bytes):  return data.decode()
    if isinstance(data, dict):   return dict(map(convert, data.items()))
    if isinstance(data, tuple):  return tuple(map(convert, data))
    if isinstance(data, list):   return list(map(convert, data))
    return data
