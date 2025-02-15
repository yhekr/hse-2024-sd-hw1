from fastapi import FastAPI, Query, HTTPException
from model import OrderData, ZoneData, ExecuterProfile, CancelStatus
import random
from typing import Optional
import uvicorn

app = FastAPI()

@app.get("/order-data")
async def get_order_data(id: Optional[str] = Query(None)):
    if not id:
        raise HTTPException(status_code=400, detail="ID parameter is required.")
    return OrderData(id=id, user_id="some-user-id", zone_id="zone-123", base_coin_amount=100.0)

@app.get("/zone-data")
async def get_zone_data(id: Optional[str] = Query(None)):
    if not id:
        raise HTTPException(status_code=400, detail="ID parameter is required.")
    return ZoneData(id=id, coin_coeff=2.0, display_name="Fancy Zone")

@app.get("/executer-profile")
async def get_executer_profile(id: Optional[str] = Query(None)):
    if not id:
        raise HTTPException(status_code=400, detail="ID parameter is required.")
    return ExecuterProfile(id=id, tags=["top-coin-expert"], rating=8.5)

@app.get("/configs")
async def get_configs():
    return {"coin_coeff_settings": {"maximum": "3", "fallback": "1"}}

@app.get("/toll-roads")
async def get_toll_roads(zone_display_name: Optional[str] = Query(None)):
    bonus = 50 if random.random() > 0.1 else 0
    return {"bonus_amount": bonus}

@app.get("/cancel-order")
async def cancel_order(order_id: Optional[str] = Query(None)):
    if random.randint(0, 20) > 0:
        print(f"Order {order_id} has canceled successfully!")
        return CancelStatus(order_id=order_id, status="success")
    else:
        print(f"Error on delivering order {order_id}")
        raise HTTPException(status_code=500, detail='Internal error')


uvicorn.run(app, host="0.0.0.0", port=3629, log_level="info")
