import time
import uuid
from datetime import datetime
import data_requests as dr
from model import AssignedOrder
from db import database as db

MAGIC_CONSTANT = 8

db.init_db()

def handle_assign_order_request(order_id: str, executer_id: str, locale: str):
    # quite a sequential execution of requests, could be improved!
    order_data = dr.get_order_data(order_id)

    zone_info = dr.get_zone_info(order_data.zone_id)

    executer_profile = dr.get_executer_profile(executer_id)

    toll_roads = dr.get_toll_roads(zone_info.display_name)

    configs = dr.get_configs()

    # all fetching is done, finally....
    # start building actual response

    # adjust coin_coeff with configuration settings
    actual_coin_coeff = zone_info.coin_coeff
    if configs.coin_coeff_settings is not None:
        actual_coin_coeff = min(float(configs.coin_coeff_settings['maximum']), actual_coin_coeff)
    final_coin_amount = order_data.base_coin_amount * actual_coin_coeff + toll_roads.bonus_amount

    order = AssignedOrder(
        str(uuid.uuid4()),
        order_id,
        executer_id,
        actual_coin_coeff,
        toll_roads.bonus_amount,
        final_coin_amount,
        '',
        datetime.now(),
        None
    )

    if executer_profile.rating >= MAGIC_CONSTANT:
        order.route_information = f'Order at zone "{zone_info.display_name}"'
    else:
        order.route_information = f'Order at somewhere'

    print(f'>> New order handled! {order}')

    # persisting order!
    db.save_order_to_db(order)


def handle_acquire_order_request(executer_id: str):
    try:
        # race condition is possible here!
        order_id = db.get_latest_order_id_for_executer(executer_id)
        if order_id:
            order_data = db.get_order_from_db(order_id)
            order_data.acquire_time = datetime.now()
            db.save_order_to_db(order_data)

            print(f'>> Order acquired! Acquire time == {order_data.acquire_time - order_data.assign_time}')
            return order_data
    except KeyError:
        print(f'Order for executer ID "{executer_id}" not found!')
        return None


def handle_cancel_order_request(order_id: str):
    # race condition is possible here!
    order_data = db.get_order_from_db(order_id)
    if order_data:
        db.delete_order_from_db(order_id)
        print(f'>> Order was cancelled!')
        return order_data
    else:
        print(f'Order ID "{order_id}" not found!')
        return None


if __name__ == '__main__':
    print('> Starting first scenario! <')
    handle_assign_order_request('some-order-id', 'some-executer-id', 'en-US')

    time.sleep(1)
    handle_acquire_order_request('some-executer-id')

    print('< First scenario is over!\n\n')

    print('> Starting second scenario! <')
    # second scenario
    handle_assign_order_request('some-order-id-to-cancel', 'another-executer-id', 'en-US')

    time.sleep(1)
    handle_cancel_order_request('some-order-id-to-cancel')
    print('< Second scenario is over!\n\n')

db.close_db()
