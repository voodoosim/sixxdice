from db.db_pool import DatabasePool


class Database:
    def __init__(self, db_name='game_database.db'):
        self.db_name = db_name
        self.pool = DatabasePool(db_name)

    async def init_db(self):
        await self.pool.initialize()
        async with self.pool.acquire() as conn:
            await conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    hearts INTEGER DEFAULT 0,
                    checked_in INTEGER DEFAULT 0,
                    last_check_in_date TEXT,
                    check_in_count INTEGER DEFAULT 0,
                    consecutive_check_ins INTEGER DEFAULT 0,
                    total_messages INTEGER DEFAULT 0,
                    full_name TEXT DEFAULT '',
                    username TEXT,
                    wins INTEGER DEFAULT 0,
                    losses INTEGER DEFAULT 0
                )
            ''')
            await conn.commit()

    async def close_all(self):
        await self.pool.close_all()
