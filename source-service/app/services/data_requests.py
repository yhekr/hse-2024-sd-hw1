import os
import json

import requests
from models.model import OrderData, ZoneData, ExecuterProfile, ConfigMap, TollRoadsData
from request_handler import RequestHandler
from cache import set_cache, get_cache

mock_host = os.getenv("MOCK_SERVER_HOST", "mock-server")
mock_port = os.getenv("MOCK_SERVER_PORT", "3629")

order_http = f'http://{mock_host}:{mock_port}/order-data'
zone_http = f'http://{mock_host}:{mock_port}/zone-data'
executer_http = f'http://{mock_host}:{mock_port}/executer-profile'
config_http = f'http://{mock_host}:{mock_port}/configs'
toll_roads_http = f'http://{mock_host}:{mock_port}/toll-roads'

def get_order_data(order_id: str) -> OrderData:
    data = RequestHandler.fetch_data(order_http, params={'id': order_id})
    return OrderData(
        id=order_id,
        zone_id=data.get('zone_id', ''),
        user_id=data.get('user_id', ''),
        base_coin_amount=data.get('base_coin_amount', 0.0)
    )

def get_zone_info(zone_id: str) -> ZoneData:
    data = RequestHandler.fetch_data(zone_http, params={'id': zone_id})
    return ZoneData(
        id=zone_id,
        coin_coeff=data.get('coin_coeff', 1.0),
        display_name=data.get('display_name', 'Unknown')
    )

def get_executer_profile(executer_id: str) -> ExecuterProfile:
    data = RequestHandler.fetch_data(executer_http, params={'id': executer_id})
    return ExecuterProfile(
        id=executer_id,
        tags=data.get('tags', []),
        rating=data.get('rating', 0.0)
    )

def get_configs() -> ConfigMap:
    cached_data = get_cache()
    if cached_data:
        config_data = json.loads(cached_data)
        return ConfigMap(coin_coeff_settings=config_data["coin_coeff_settings"])
    config_data = RequestHandler.fetch_data(config_http)
    set_cache(json.dumps(config_data))
    return ConfigMap(coin_coeff_settings=config_data["coin_coeff_settings"])

def get_toll_roads(zone_display_name: str) -> TollRoadsData:
    data = RequestHandler.fetch_data(toll_roads_http, params={'zone_display_name': zone_display_name})
    return TollRoadsData(
        bonus_amount=data.get('bonus_amount', 0.0)
    )
