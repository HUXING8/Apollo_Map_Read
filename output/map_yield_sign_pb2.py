# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: map_yield_sign.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    1,
    '',
    'map_yield_sign.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import output.map_id_pb2 as map__id__pb2
import output.map_geometry_pb2 as map__geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14map_yield_sign.proto\x12\x0c\x61pollo.hdmap\x1a\x0cmap_id.proto\x1a\x12map_geometry.proto\"w\n\tYieldSign\x12\x1c\n\x02id\x18\x01 \x01(\x0b\x32\x10.apollo.hdmap.Id\x12&\n\tstop_line\x18\x02 \x03(\x0b\x32\x13.apollo.hdmap.Curve\x12$\n\noverlap_id\x18\x03 \x03(\x0b\x32\x10.apollo.hdmap.Id')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'map_yield_sign_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_YIELDSIGN']._serialized_start=72
  _globals['_YIELDSIGN']._serialized_end=191
# @@protoc_insertion_point(module_scope)
