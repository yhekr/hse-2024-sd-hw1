from models.model import Info
from services import data_requests
import asyncio


def get_order_zone_toll(request):
    order_data = data_requests.get_order_data(request.order_id)
    zone_info = data_requests.get_zone_info(order_data.zone_id)
    toll_roads = data_requests.get_toll_roads(zone_info.display_name)

    return order_data, zone_info, toll_roads


async def get_order_info(request):
    order_zone_toll_task = asyncio.create_task(get_order_zone_toll(request))
    executer_profile_task = asyncio.create_task(data_requests.get_executer_profile(request.executer_id))
    configs_task = asyncio.create_task(data_requests.get_configs())

    order_data, zone_info, toll_roads, executer_profile, configs = await asyncio.gather(
        order_zone_toll_task, executer_profile_task, configs_task
    )

    return Info(
        order_data=order_data,
        zone_data=zone_info,
        toll_roads_data=toll_roads,
        executer_profile=executer_profile,
        config_map=configs
    )
