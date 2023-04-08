from pydantic import BaseModel, constr


class PhoneSchema(BaseModel):
    """Phone schema."""

    phone: constr(regex=r'^[0-9]{11}$')


class AddressSchema(BaseModel):
    """Address schema."""

    address: str | None


class PhoneAddressSchema(AddressSchema, PhoneSchema):
    """Phone and address schema."""
    pass