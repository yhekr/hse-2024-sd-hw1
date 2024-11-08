from fastapi import FastAPI, HTTPException
from models.request_models import OrderRequest, AcquireRequest, CancelRequest
from services import order_handler

app = FastAPI()

@app.post("/assign-order/")
async def assign_order(request: OrderRequest):
    order = order_handler.handle_assign_order_request(request.order_id, request.executer_id, request.locale)
    if order:
        return {"message": "Order assigned successfully", "order": order}
    raise HTTPException(status_code=500, detail="Failed to assign order.")

@app.post("/acquire-order/")
async def acquire_order(request: AcquireRequest):
    order = order_handler.handle_acquire_order_request(request.executer_id)
    if order:
        return {"message": "Order acquired successfully", "order": order}
    raise HTTPException(status_code=404, detail="Order not found.")

@app.post("/cancel-order/")
async def cancel_order(request: CancelRequest):
    order = order_handler.handle_cancel_order_request(request.order_id)
    if order:
        return {"message": "Order cancelled successfully", "order": order}
    raise HTTPException(status_code=404, detail="Order not found.")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)