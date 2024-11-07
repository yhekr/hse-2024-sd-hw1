from pydantic import BaseModel

class OrderRequest(BaseModel):
    order_id: str
    executer_id: str
    locale: str

class AcquireRequest(BaseModel):
    executer_id: str

class CancelRequest(BaseModel):
    order_id: str
