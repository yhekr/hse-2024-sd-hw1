from models.model import CancellationPayload, AssignedOrder

def assemblePayload(order_data: AssignedOrder):
    return CancellationPayload(
        order_id=order_data.order_id
    )