from typing import Optional
from pydantic import BaseModel


class Category(BaseModel):
    id: Optional[str]
    name: str
    description: str
    active: Optional[bool]
