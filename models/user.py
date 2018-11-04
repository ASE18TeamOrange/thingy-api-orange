from models.database import Database

class User:

    async def create(self, name, pwd):
        redis = Database()
        if not self.exists(name, pwd):
            redis.insert(name, pwd)
            return True
        return False

    async def delete(self, name, pwd):
        redis = Database()
        if self.exists(name, pwd):
            redis.delete(name)
            return True
        return False

    async def exists(self, name, pwd):
        redis = Database()
        user = redis.get(name)
        if user is not None:
            return user.pwd == pwd
        return False
