# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alvinchow_backend_protobuf/alvinchow_backend.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from alvinchow_backend_protobuf import common_pb2 as alvinchow__backend__protobuf_dot_common__pb2
from alvinchow_backend_protobuf import foo_pb2 as alvinchow__backend__protobuf_dot_foo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='alvinchow_backend_protobuf/alvinchow_backend.proto',
  package='alvinchow_backend',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2alvinchow_backend_protobuf/alvinchow_backend.proto\x12\x11\x61lvinchow_backend\x1a\x1bgoogle/protobuf/empty.proto\x1a\'alvinchow_backend_protobuf/common.proto\x1a$alvinchow_backend_protobuf/foo.proto2\x95\x01\n\x10\x41lvinChowService\x12\x41\n\x04Ping\x12\x16.google.protobuf.Empty\x1a!.alvinchow_backend.SimpleResponse\x12>\n\x06GetFoo\x12\x1c.alvinchow_backend.IdRequest\x1a\x16.alvinchow_backend.Foob\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,alvinchow__backend__protobuf_dot_common__pb2.DESCRIPTOR,alvinchow__backend__protobuf_dot_foo__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ALVINCHOWSERVICE = _descriptor.ServiceDescriptor(
  name='AlvinChowService',
  full_name='alvinchow_backend.AlvinChowService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=182,
  serialized_end=331,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='alvinchow_backend.AlvinChowService.Ping',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=alvinchow__backend__protobuf_dot_common__pb2._SIMPLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetFoo',
    full_name='alvinchow_backend.AlvinChowService.GetFoo',
    index=1,
    containing_service=None,
    input_type=alvinchow__backend__protobuf_dot_common__pb2._IDREQUEST,
    output_type=alvinchow__backend__protobuf_dot_foo__pb2._FOO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ALVINCHOWSERVICE)

DESCRIPTOR.services_by_name['AlvinChowService'] = _ALVINCHOWSERVICE

# @@protoc_insertion_point(module_scope)