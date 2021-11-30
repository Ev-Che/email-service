from typing import Optional

from pydantic import BaseModel, Field


class Mail(BaseModel):
    receiver: str
    topic: Optional[str] = Field(max_length=50)
    message: Optional[str] = Field(max_length=300)
