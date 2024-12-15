import aiosqlite


class DatabasePool:
    def __init__(self, db_name):
        self.db_name = db_name
        self.pool = None

    async def initialize(self):
        self.pool = await aiosqlite.connect(self.db_name)

    async def acquire(self):
        return self.pool

    async def close_all(self):
        if self.pool:
            await self.pool.close()
