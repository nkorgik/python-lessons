import asyncio
import asyncpg

from typing_extensions import Self

class Database:
    def connect(self):
        pass
    
    def query(self, query):
        pass
    
    
class UserRepository:
    def __init__(self, db_connection) -> None:
        self.db_connection = db_connection
        
    def get_users(self):
        return self.db_connection.query('SELECT * FROM users;')
    
    
class UserService:
    def __init__(self, user_repository) -> None:
        self.user_repository = user_repository
        
    def get_all_users(self):
        return self.user_repository.get_users()
    
    
database = Database()
user_repository = UserRepository(database)
user_service = UserService(user_repository)

users = user_service.get_all_users()


# Singleton in conjunction with Dependency Injection

class DatabaseEngine:
    _instance = None
    _pool = None
    
    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    async def get_pool(self, user, password, database, host, port):
        if self._pool is None:
            self._pool = await asyncpg.create_pool(
                user=user,
                password=password,
                database=database,
                host=host,
                port=port,
                min_size=5,
                max_size=10
            )
        
        return self._pool
    
    async def close_pool(self):
        if self._pool is not None:
            await self._pool.close()
            self._pool = None
            

class UserRepository:
    def __init__(self, db_connection_pool) -> None:
        self.db_connection_pool = db_connection_pool
        
    async def get_users(self):
        async with self.db_connection_pool.acquire() as conn:
            return await conn.fetch('SELECT * FROM users')
        

class UserService:
    def __init__(self, user_repository) -> None:
        self.user_repository = user_repository
        
    async def get_all_users(self):
        return await self.user_repository.get_users()
    
    
async def main(database: DatabaseEngine):
    pool = await database.get_pool(
        user='user',
        password='password',
        database='database',
        host='host',
        port='port'
    )
    
    user_repository = UserRepository(pool)
    user_service = UserService(user_repository)
    
    users = await user_service.get_all_users()
    print(users)
    
    await database.close_pool()
    

if __name__ == '__main__':
    database = DatabaseEngine()
    asyncio.run(main(database))
