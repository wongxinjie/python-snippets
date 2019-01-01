# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: key.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='key.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\tkey.proto\"\x1b\n\x0cTokenRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"\x1e\n\rTokenResponse\x12\r\n\x05token\x18\x01 \x01(\t24\n\x05Token\x12+\n\x08generate\x12\r.TokenRequest\x1a\x0e.TokenResponse\"\x00\x62\x06proto3')
)




_TOKENREQUEST = _descriptor.Descriptor(
  name='TokenRequest',
  full_name='TokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='TokenRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13,
  serialized_end=40,
)


_TOKENRESPONSE = _descriptor.Descriptor(
  name='TokenResponse',
  full_name='TokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='TokenResponse.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=72,
)

DESCRIPTOR.message_types_by_name['TokenRequest'] = _TOKENREQUEST
DESCRIPTOR.message_types_by_name['TokenResponse'] = _TOKENRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TokenRequest = _reflection.GeneratedProtocolMessageType('TokenRequest', (_message.Message,), dict(
  DESCRIPTOR = _TOKENREQUEST,
  __module__ = 'key_pb2'
  # @@protoc_insertion_point(class_scope:TokenRequest)
  ))
_sym_db.RegisterMessage(TokenRequest)

TokenResponse = _reflection.GeneratedProtocolMessageType('TokenResponse', (_message.Message,), dict(
  DESCRIPTOR = _TOKENRESPONSE,
  __module__ = 'key_pb2'
  # @@protoc_insertion_point(class_scope:TokenResponse)
  ))
_sym_db.RegisterMessage(TokenResponse)



_TOKEN = _descriptor.ServiceDescriptor(
  name='Token',
  full_name='Token',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=74,
  serialized_end=126,
  methods=[
  _descriptor.MethodDescriptor(
    name='generate',
    full_name='Token.generate',
    index=0,
    containing_service=None,
    input_type=_TOKENREQUEST,
    output_type=_TOKENRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TOKEN)

DESCRIPTOR.services_by_name['Token'] = _TOKEN

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class TokenStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.generate = channel.unary_unary(
          '/Token/generate',
          request_serializer=TokenRequest.SerializeToString,
          response_deserializer=TokenResponse.FromString,
          )


  class TokenServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def generate(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_TokenServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'generate': grpc.unary_unary_rpc_method_handler(
            servicer.generate,
            request_deserializer=TokenRequest.FromString,
            response_serializer=TokenResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Token', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaTokenServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def generate(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaTokenStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def generate(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    generate.future = None


  def beta_create_Token_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Token', 'generate'): TokenRequest.FromString,
    }
    response_serializers = {
      ('Token', 'generate'): TokenResponse.SerializeToString,
    }
    method_implementations = {
      ('Token', 'generate'): face_utilities.unary_unary_inline(servicer.generate),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Token_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Token', 'generate'): TokenRequest.SerializeToString,
    }
    response_deserializers = {
      ('Token', 'generate'): TokenResponse.FromString,
    }
    cardinalities = {
      'generate': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Token', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)