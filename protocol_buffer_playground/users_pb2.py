# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0busers.proto\x12\x0e\x63om.realpython\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8e\x01\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12*\n\x08language\x18\x04 \x01(\x0e\x32\x18.com.realpython.Language\x12\x31\n\rregistered_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\",\n\x05Users\x12#\n\x05users\x18\x01 \x03(\x0b\x32\x14.com.realpython.User*:\n\x08Language\x12\x06\n\x02\x44\x45\x10\x00\x12\x06\n\x02\x45N\x10\x01\x12\x06\n\x02\x45S\x10\x02\x12\x06\n\x02\x46R\x10\x03\x12\x06\n\x02IT\x10\x04\x12\x06\n\x02PL\x10\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'users_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LANGUAGE._serialized_start=255
  _LANGUAGE._serialized_end=313
  _USER._serialized_start=65
  _USER._serialized_end=207
  _USERS._serialized_start=209
  _USERS._serialized_end=253
# @@protoc_insertion_point(module_scope)
