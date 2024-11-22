from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrderPrice(_message.Message):
    __slots__ = ("base_order_price", "coin_coef", "coin_bonus_amount", "final_order_price")
    BASE_ORDER_PRICE_FIELD_NUMBER: _ClassVar[int]
    COIN_COEF_FIELD_NUMBER: _ClassVar[int]
    COIN_BONUS_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    FINAL_ORDER_PRICE_FIELD_NUMBER: _ClassVar[int]
    base_order_price: float
    coin_coef: float
    coin_bonus_amount: float
    final_order_price: float
    def __init__(self, base_order_price: _Optional[float] = ..., coin_coef: _Optional[float] = ..., coin_bonus_amount: _Optional[float] = ..., final_order_price: _Optional[float] = ...) -> None: ...

class ExecuterProfile(_message.Message):
    __slots__ = ("id", "tags", "rating")
    ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    id: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    rating: float
    def __init__(self, id: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., rating: _Optional[float] = ...) -> None: ...

class GetOrderInfoRequest(_message.Message):
    __slots__ = ("order_id", "executer_id")
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    executer_id: str
    def __init__(self, order_id: _Optional[str] = ..., executer_id: _Optional[str] = ...) -> None: ...

class GetOrderInfoResponse(_message.Message):
    __slots__ = ("order_price", "zone_display_name", "executor_profile")
    ORDER_PRICE_FIELD_NUMBER: _ClassVar[int]
    ZONE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTOR_PROFILE_FIELD_NUMBER: _ClassVar[int]
    order_price: OrderPrice
    zone_display_name: str
    executor_profile: ExecuterProfile
    def __init__(self, order_price: _Optional[_Union[OrderPrice, _Mapping]] = ..., zone_display_name: _Optional[str] = ..., executor_profile: _Optional[_Union[ExecuterProfile, _Mapping]] = ...) -> None: ...
