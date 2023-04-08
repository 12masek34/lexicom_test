from fastapi import Depends, FastAPI, status
from redis.asyncio import Redis

from db import get_db
from schema import AddressSchema, PhoneAddressSchema, PhoneSchema
from services import (
    create_new_data,
    get_address,
    update_exist_address,
    validate_exist_address,
    validate_miss_address,
)


app = FastAPI()


@app.get('/check_data', status_code=status.HTTP_200_OK)
async def check_address(phone: PhoneSchema = Depends(), db: Redis = Depends(get_db)) -> str | None:
    """Get address by phone number."""

    address = await get_address(db, phone.phone)
    validate_miss_address(address)

    return address


@app.post('/write_data', status_code=status.HTTP_201_CREATED)
async def create_data(data: PhoneAddressSchema, db: Redis = Depends(get_db)) -> PhoneAddressSchema:
    """Write phone number and address."""

    address = await get_address(db, data.phone)
    validate_exist_address(address)
    await create_new_data(db, data)

    return data


@app.patch('/write_data', status_code=status.HTTP_200_OK)
async def update_address(data: PhoneAddressSchema, db: Redis = Depends(get_db)) -> AddressSchema:
    """Update address by phone number."""

    address = await get_address(db, data.phone)
    validate_miss_address(address)
    await update_exist_address(db, data.phone, data.address)

    return data
