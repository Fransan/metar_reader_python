from __future__ import annotations
from pydantic import BaseModel

class Metar(BaseModel):
    station: str
    time: str
    raw_string: str
