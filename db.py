import os

from redis.asyncio import Redis
from dotenv import load_dotenv


load_dotenv()


def get_db() -> Redis:
    """Get connection database."""

    host = os.getenv('host')
    port = os.getenv('port')

    return Redis(host=host, port=port)
