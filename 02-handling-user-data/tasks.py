import os
import asyncio
from invoke import task
from dotenv import load_dotenv

async def _count(dsn: str) -> int:
    import asyncpg
    conn = await asyncpg.connect(dsn)
    try:
        return int(await conn.fetchval('SELECT COUNT(*) FROM "User"') or 0)
    finally:
        await conn.close()


@task
def db_verify(_):
    """Verify DB is reachable and print total users."""
    load_dotenv()
    dsn = os.getenv("DATABASE_URL") or (
        f"postgresql://{os.getenv('POSTGRES_USER','postgres')}:{os.getenv('POSTGRES_PASSWORD','postgres')}@"
        f"{os.getenv('POSTGRES_HOST','localhost')}:{os.getenv('POSTGRES_PORT','5432')}/{os.getenv('POSTGRES_DB','postgres')}"
    )
    count = asyncio.run(_count(dsn))
    print(f"Database found. Total users: {count}")
