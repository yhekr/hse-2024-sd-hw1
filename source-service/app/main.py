from fastapi import FastAPI
from app.data_requests import get_order_data, get_zone_info, get_executer_profile, get_configs, get_toll_roads

app = FastAPI()

@app.get("/order-data")
async def order_data(order_id: str):
    return get_order_data(order_id)

@app.get("/zone-data")
async def zone_data(zone_id: str):
    return get_zone_info(zone_id)

@app.get("/executer-profile")
async def executer_profile(executer_id: str):
    return get_executer_profile(executer_id)

@app.get("/configs")
async def configs():
    return get_configs()

@app.get("/toll-roads")
async def toll_roads(zone_display_name: str):
    return get_toll_roads(zone_display_name)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=3629, log_level='info')
