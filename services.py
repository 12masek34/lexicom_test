from redis.asyncio import Redis
from fastapi import HTTPException, status

from schema import PhoneAddressSchema


async def get_address(db: Redis, phone: str) -> str | None:
    """Get address by phone number from db."""
    return await db.get(phone)


async def create_new_data(db: Redis, data: PhoneAddressSchema) -> None:
    """Saves new data to the db."""
    await db.set(data.phone, data.address)


async def update_exist_address(db: Redis, phone: str, address: str) -> None:
    """Update address by phone number."""
    await db.set(phone, address)


def validate_exist_address(address: str | None) -> None:
    """Checks that the addresses do not exist."""

    if address is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Phone number alredy exists.')


def validate_miss_address(address: str | None) -> None:
    """Checks that the address exists."""

    if address is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Phone not found.')
