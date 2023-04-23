import asyncio 
import asyncpg

from typing_extensions import Self


class Singleton:
    _instance = None 
    is_initialized = False
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self) -> None:
        if not self.is_initialized:
            self.data = []
            Singleton.is_initialized = True
            
    
singleton1 = Singleton()
singleton2 = Singleton()

singleton1.data.append('Hello')
singleton2.data.append('World!')

print(singleton1.data) # ['Hello', 'World!']
print(singleton2.data) # ['Hello', 'World!']

print(singleton1 is singleton2) # True


# Database Engine

class DatabaseEngine:
    """
    Singleton pattern for using Asynpg driver
    
    _engine - is an abstract instance of our Database, not a conn
    """
    _engine = None
    _pool = None
    
    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return 
    
    async def get_pool(self):
        if self._pool is None:
            self._pool = await asyncpg.create_pool(
                user='user',
                password='password',
                database='database',
                host='host',
                port='5432',
                min_size=5,
                max_size=10
            )
        
        return self._pool
    
    async def close(self):
        if self._pool is not None:
            await self._pool.close()
            self._pool = None
            

async def main():
    engine = DatabaseEngine()
    database_pool = await engine.get_pool()
    
    async with database_pool.acquire() as conn:
        result = await conn.fetch('SELECT * FROM your_table')
        print(result)
        
    await database_pool.close()
    

if __name__ == '__main__':
    asyncio.run(main())
    