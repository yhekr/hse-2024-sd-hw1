from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AssignedOrder(BaseModel):
    assign_order_id: str
    order_id: str
    executer_id: str
    coin_coeff: float
    coin_bonus_amount: float
    final_coin_amount: float
    route_information: str
    assign_time: datetime
    acquire_time: Optional[datetime]
