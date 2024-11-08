# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_requests.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x64\x61ta_requests.proto\x12\x0c\x64\x61tarequests\"\x07\n\x05\x45mpty\" \n\x0cOrderRequest\x12\x10\n\x08order_id\x18\x01 \x01(\t\"S\n\tOrderData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0f\n\x07zone_id\x18\x03 \x01(\t\x12\x18\n\x10\x62\x61se_coin_amount\x18\x04 \x01(\x02\"\x1e\n\x0bZoneRequest\x12\x0f\n\x07zone_id\x18\x01 \x01(\t\"@\n\x08ZoneData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncoin_coeff\x18\x02 \x01(\x02\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\"&\n\x0f\x45xecuterRequest\x12\x13\n\x0b\x65xecuter_id\x18\x01 \x01(\t\";\n\x0f\x45xecuterProfile\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04tags\x18\x02 \x03(\t\x12\x0e\n\x06rating\x18\x03 \x01(\x02\"\x94\x01\n\nConfigData\x12L\n\x13\x63oin_coeff_settings\x18\x01 \x03(\x0b\x32/.datarequests.ConfigData.CoinCoeffSettingsEntry\x1a\x38\n\x16\x43oinCoeffSettingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"-\n\x10TollRoadsRequest\x12\x19\n\x11zone_display_name\x18\x01 \x01(\t\"%\n\rTollRoadsData\x12\x14\n\x0c\x62onus_amount\x18\x01 \x01(\x02\x32\xfa\x02\n\x13\x44\x61taRequestsService\x12\x43\n\x0cGetOrderData\x12\x1a.datarequests.OrderRequest\x1a\x17.datarequests.OrderData\x12@\n\x0bGetZoneInfo\x12\x19.datarequests.ZoneRequest\x1a\x16.datarequests.ZoneData\x12R\n\x12GetExecuterProfile\x12\x1d.datarequests.ExecuterRequest\x1a\x1d.datarequests.ExecuterProfile\x12;\n\nGetConfigs\x12\x13.datarequests.Empty\x1a\x18.datarequests.ConfigData\x12K\n\x0cGetTollRoads\x12\x1e.datarequests.TollRoadsRequest\x1a\x1b.datarequests.TollRoadsDatab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'data_requests_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIGDATA_COINCOEFFSETTINGSENTRY._options = None
  _CONFIGDATA_COINCOEFFSETTINGSENTRY._serialized_options = b'8\001'
  _globals['_EMPTY']._serialized_start=37
  _globals['_EMPTY']._serialized_end=44
  _globals['_ORDERREQUEST']._serialized_start=46
  _globals['_ORDERREQUEST']._serialized_end=78
  _globals['_ORDERDATA']._serialized_start=80
  _globals['_ORDERDATA']._serialized_end=163
  _globals['_ZONEREQUEST']._serialized_start=165
  _globals['_ZONEREQUEST']._serialized_end=195
  _globals['_ZONEDATA']._serialized_start=197
  _globals['_ZONEDATA']._serialized_end=261
  _globals['_EXECUTERREQUEST']._serialized_start=263
  _globals['_EXECUTERREQUEST']._serialized_end=301
  _globals['_EXECUTERPROFILE']._serialized_start=303
  _globals['_EXECUTERPROFILE']._serialized_end=362
  _globals['_CONFIGDATA']._serialized_start=365
  _globals['_CONFIGDATA']._serialized_end=513
  _globals['_CONFIGDATA_COINCOEFFSETTINGSENTRY']._serialized_start=457
  _globals['_CONFIGDATA_COINCOEFFSETTINGSENTRY']._serialized_end=513
  _globals['_TOLLROADSREQUEST']._serialized_start=515
  _globals['_TOLLROADSREQUEST']._serialized_end=560
  _globals['_TOLLROADSDATA']._serialized_start=562
  _globals['_TOLLROADSDATA']._serialized_end=599
  _globals['_DATAREQUESTSSERVICE']._serialized_start=602
  _globals['_DATAREQUESTSSERVICE']._serialized_end=980
# @@protoc_insertion_point(module_scope)
