def calculateFinalPrice(order_info):
    actual_coin_coeff = order_info.zone_data.coin_coeff
    if order_info.config_map.coin_coeff_settings:
        actual_coin_coeff = min(float(order_info.config_map.coin_coeff_settings.get('maximum', '1')), actual_coin_coeff)
    return order_info.order_data.base_coin_amount * actual_coin_coeff + order_info.toll_roads_data.bonus_amount