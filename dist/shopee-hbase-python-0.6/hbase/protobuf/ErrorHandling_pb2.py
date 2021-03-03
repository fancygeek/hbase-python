# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ErrorHandling.proto

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
  name='ErrorHandling.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x13\x45rrorHandling.proto\"p\n\x18StackTraceElementMessage\x12\x17\n\x0f\x64\x65\x63laring_class\x18\x01 \x01(\t\x12\x13\n\x0bmethod_name\x18\x02 \x01(\t\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12\x13\n\x0bline_number\x18\x04 \x01(\x05\"|\n\x17GenericExceptionMessage\x12\x12\n\nclass_name\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x12\n\nerror_info\x18\x03 \x01(\x0c\x12(\n\x05trace\x18\x04 \x03(\x0b\x32\x19.StackTraceElementMessage\"^\n\x17\x46oreignExceptionMessage\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x33\n\x11generic_exception\x18\x02 \x01(\x0b\x32\x18.GenericExceptionMessageBF\n*org.apache.hadoop.hbase.protobuf.generatedB\x13\x45rrorHandlingProtosH\x01\xa0\x01\x01')
)




_STACKTRACEELEMENTMESSAGE = _descriptor.Descriptor(
  name='StackTraceElementMessage',
  full_name='StackTraceElementMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='declaring_class', full_name='StackTraceElementMessage.declaring_class', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='method_name', full_name='StackTraceElementMessage.method_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_name', full_name='StackTraceElementMessage.file_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='line_number', full_name='StackTraceElementMessage.line_number', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=135,
)


_GENERICEXCEPTIONMESSAGE = _descriptor.Descriptor(
  name='GenericExceptionMessage',
  full_name='GenericExceptionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_name', full_name='GenericExceptionMessage.class_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='GenericExceptionMessage.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_info', full_name='GenericExceptionMessage.error_info', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace', full_name='GenericExceptionMessage.trace', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=261,
)


_FOREIGNEXCEPTIONMESSAGE = _descriptor.Descriptor(
  name='ForeignExceptionMessage',
  full_name='ForeignExceptionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='ForeignExceptionMessage.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generic_exception', full_name='ForeignExceptionMessage.generic_exception', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=263,
  serialized_end=357,
)

_GENERICEXCEPTIONMESSAGE.fields_by_name['trace'].message_type = _STACKTRACEELEMENTMESSAGE
_FOREIGNEXCEPTIONMESSAGE.fields_by_name['generic_exception'].message_type = _GENERICEXCEPTIONMESSAGE
DESCRIPTOR.message_types_by_name['StackTraceElementMessage'] = _STACKTRACEELEMENTMESSAGE
DESCRIPTOR.message_types_by_name['GenericExceptionMessage'] = _GENERICEXCEPTIONMESSAGE
DESCRIPTOR.message_types_by_name['ForeignExceptionMessage'] = _FOREIGNEXCEPTIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StackTraceElementMessage = _reflection.GeneratedProtocolMessageType('StackTraceElementMessage', (_message.Message,), dict(
  DESCRIPTOR = _STACKTRACEELEMENTMESSAGE,
  __module__ = 'ErrorHandling_pb2'
  # @@protoc_insertion_point(class_scope:StackTraceElementMessage)
  ))
_sym_db.RegisterMessage(StackTraceElementMessage)

GenericExceptionMessage = _reflection.GeneratedProtocolMessageType('GenericExceptionMessage', (_message.Message,), dict(
  DESCRIPTOR = _GENERICEXCEPTIONMESSAGE,
  __module__ = 'ErrorHandling_pb2'
  # @@protoc_insertion_point(class_scope:GenericExceptionMessage)
  ))
_sym_db.RegisterMessage(GenericExceptionMessage)

ForeignExceptionMessage = _reflection.GeneratedProtocolMessageType('ForeignExceptionMessage', (_message.Message,), dict(
  DESCRIPTOR = _FOREIGNEXCEPTIONMESSAGE,
  __module__ = 'ErrorHandling_pb2'
  # @@protoc_insertion_point(class_scope:ForeignExceptionMessage)
  ))
_sym_db.RegisterMessage(ForeignExceptionMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n*org.apache.hadoop.hbase.protobuf.generatedB\023ErrorHandlingProtosH\001\240\001\001'))
# @@protoc_insertion_point(module_scope)
