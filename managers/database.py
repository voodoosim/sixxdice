from db.db_pool import DatabasePool


class Database:
    def __init__(self, db_name="game_database.db"):
        self.db_name = db_name
        self.pool = DatabasePool(db_name)

    async def init_db(self):
        """데이터베이스 초기화"""
        await self.pool.initialize()
        async with self.pool.acquire() as conn:
            await conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    hearts INTEGER DEFAULT 0,
                    checked_in INTEGER DEFAULT 0,
                    last_check_in_date TEXT,
                    check_in_count INTEGER DEFAULT 0
                )
            ''')
            await conn.commit()

    async def close_all(self):
        """연결 풀 닫기"""
        await self.pool.close_all()
