import re
from pydantic import validator
from app.schemas.base import CustomBaseModel

class Category(CustomBaseModel):
    name: str
    slug: str

    @validator('slug')
    def validade_slug(cls, value):
        if not re.match('^([a-z]|-|_)+$', value):
            raise ValueError('Invalid slug')
        return value