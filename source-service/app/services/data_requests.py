import os

import requests
from models.model import OrderData, ZoneData, ExecuterProfile, ConfigMap, TollRoadsData

mock_host = os.getenv("MOCK_SERVER_HOST", "mock-server")
mock_port = os.getenv("MOCK_SERVER_PORT", "3629")

order_http = f'http://{mock_host}:{mock_port}/order-data'
zone_http = f'http://{mock_host}:{mock_port}/zone-data'
executer_http = f'http://{mock_host}:{mock_port}/executer-profile'
config_http = f'http://{mock_host}:{mock_port}/configs'
toll_roads_http = f'http://{mock_host}:{mock_port}/toll-roads'

def get_order_data(order_id: str) -> OrderData:
    raw_data = requests.get(order_http, params={'id': order_id})
    return OrderData(
        id=order_id,
        zone_id=raw_data.json()['zone_id'],
        user_id=raw_data.json()['user_id'],
        base_coin_amount=raw_data.json()['base_coin_amount']
    )

def get_zone_info(zone_id: str) -> ZoneData:
    raw_data = requests.get(zone_http, params={'id': zone_id})
    return ZoneData(
        id=zone_id,
        coin_coeff=raw_data.json()['coin_coeff'],
        display_name=raw_data.json()['display_name']
    )

def get_executer_profile(executer_id: str) -> ExecuterProfile:
    raw_data = requests.get(executer_http, params={'id': executer_id})
    return ExecuterProfile(
        id=executer_id,
        tags=raw_data.json()['tags'],
        rating=raw_data.json()['rating']
    )

def get_configs() -> ConfigMap:
    raw_data = requests.get(config_http)
    return ConfigMap(raw_data.json())

def get_toll_roads(zone_display_name: str) -> TollRoadsData:
    raw_data = requests.get(toll_roads_http, params={'zone_display_name': zone_display_name})
    return TollRoadsData(bonus_amount=raw_data.json()['bonus_amount'])
