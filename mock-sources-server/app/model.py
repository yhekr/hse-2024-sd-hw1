from pydantic import BaseModel
from typing import List, Dict, Optional


class OrderData(BaseModel):
    id: str
    user_id: str
    zone_id: str
    base_coin_amount: float


class ZoneData(BaseModel):
    id: str
    coin_coeff: float
    display_name: str


class ExecuterProfile(BaseModel):
    id: str
    tags: List[str]
    rating: float


class ConfigMap(BaseModel):
    coin_coeff_settings: Dict[str, str]


class TollRoadsData(BaseModel):
    bonus_amount: float
