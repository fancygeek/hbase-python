# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AccessControl.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import HBase_pb2 as HBase__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='AccessControl.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x13\x41\x63\x63\x65ssControl.proto\x1a\x0bHBase.proto\"\xa8\x02\n\nPermission\x12\x1e\n\x04type\x18\x01 \x02(\x0e\x32\x10.Permission.Type\x12,\n\x11global_permission\x18\x02 \x01(\x0b\x32\x11.GlobalPermission\x12\x32\n\x14namespace_permission\x18\x03 \x01(\x0b\x32\x14.NamespacePermission\x12*\n\x10table_permission\x18\x04 \x01(\x0b\x32\x10.TablePermission\">\n\x06\x41\x63tion\x12\x08\n\x04READ\x10\x00\x12\t\n\x05WRITE\x10\x01\x12\x08\n\x04\x45XEC\x10\x02\x12\n\n\x06\x43REATE\x10\x03\x12\t\n\x05\x41\x44MIN\x10\x04\",\n\x04Type\x12\n\n\x06Global\x10\x01\x12\r\n\tNamespace\x10\x02\x12\t\n\x05Table\x10\x03\"x\n\x0fTablePermission\x12\x1e\n\ntable_name\x18\x01 \x01(\x0b\x32\n.TableName\x12\x0e\n\x06\x66\x61mily\x18\x02 \x01(\x0c\x12\x11\n\tqualifier\x18\x03 \x01(\x0c\x12\"\n\x06\x61\x63tion\x18\x04 \x03(\x0e\x32\x12.Permission.Action\"Q\n\x13NamespacePermission\x12\x16\n\x0enamespace_name\x18\x01 \x01(\x0c\x12\"\n\x06\x61\x63tion\x18\x02 \x03(\x0e\x32\x12.Permission.Action\"6\n\x10GlobalPermission\x12\"\n\x06\x61\x63tion\x18\x01 \x03(\x0e\x32\x12.Permission.Action\"?\n\x0eUserPermission\x12\x0c\n\x04user\x18\x01 \x02(\x0c\x12\x1f\n\npermission\x18\x03 \x02(\x0b\x32\x0b.Permission\"\x98\x01\n\x13UsersAndPermissions\x12>\n\x10user_permissions\x18\x01 \x03(\x0b\x32$.UsersAndPermissions.UserPermissions\x1a\x41\n\x0fUserPermissions\x12\x0c\n\x04user\x18\x01 \x02(\x0c\x12 \n\x0bpermissions\x18\x02 \x03(\x0b\x32\x0b.Permission\"8\n\x0cGrantRequest\x12(\n\x0fuser_permission\x18\x01 \x02(\x0b\x32\x0f.UserPermission\"\x0f\n\rGrantResponse\"9\n\rRevokeRequest\x12(\n\x0fuser_permission\x18\x01 \x02(\x0b\x32\x0f.UserPermission\"\x10\n\x0eRevokeResponse\"s\n\x19GetUserPermissionsRequest\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.Permission.Type\x12\x1e\n\ntable_name\x18\x02 \x01(\x0b\x32\n.TableName\x12\x16\n\x0enamespace_name\x18\x03 \x01(\x0c\"F\n\x1aGetUserPermissionsResponse\x12(\n\x0fuser_permission\x18\x01 \x03(\x0b\x32\x0f.UserPermission\":\n\x17\x43heckPermissionsRequest\x12\x1f\n\npermission\x18\x01 \x03(\x0b\x32\x0b.Permission\"\x1a\n\x18\x43heckPermissionsResponse2\x81\x02\n\x14\x41\x63\x63\x65ssControlService\x12&\n\x05Grant\x12\r.GrantRequest\x1a\x0e.GrantResponse\x12)\n\x06Revoke\x12\x0e.RevokeRequest\x1a\x0f.RevokeResponse\x12M\n\x12GetUserPermissions\x12\x1a.GetUserPermissionsRequest\x1a\x1b.GetUserPermissionsResponse\x12G\n\x10\x43heckPermissions\x12\x18.CheckPermissionsRequest\x1a\x19.CheckPermissionsResponseBI\n*org.apache.hadoop.hbase.protobuf.generatedB\x13\x41\x63\x63\x65ssControlProtosH\x01\x88\x01\x01\xa0\x01\x01')
  ,
  dependencies=[HBase__pb2.DESCRIPTOR,])



_PERMISSION_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='Permission.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='READ', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRITE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXEC', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADMIN', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=225,
  serialized_end=287,
)
_sym_db.RegisterEnumDescriptor(_PERMISSION_ACTION)

_PERMISSION_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Permission.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Global', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Namespace', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Table', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=289,
  serialized_end=333,
)
_sym_db.RegisterEnumDescriptor(_PERMISSION_TYPE)


_PERMISSION = _descriptor.Descriptor(
  name='Permission',
  full_name='Permission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Permission.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global_permission', full_name='Permission.global_permission', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namespace_permission', full_name='Permission.namespace_permission', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table_permission', full_name='Permission.table_permission', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PERMISSION_ACTION,
    _PERMISSION_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=333,
)


_TABLEPERMISSION = _descriptor.Descriptor(
  name='TablePermission',
  full_name='TablePermission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_name', full_name='TablePermission.table_name', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='family', full_name='TablePermission.family', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qualifier', full_name='TablePermission.qualifier', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='TablePermission.action', index=3,
      number=4, type=14, cpp_type=8, label=3,
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
  serialized_start=335,
  serialized_end=455,
)


_NAMESPACEPERMISSION = _descriptor.Descriptor(
  name='NamespacePermission',
  full_name='NamespacePermission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace_name', full_name='NamespacePermission.namespace_name', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='NamespacePermission.action', index=1,
      number=2, type=14, cpp_type=8, label=3,
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
  serialized_start=457,
  serialized_end=538,
)


_GLOBALPERMISSION = _descriptor.Descriptor(
  name='GlobalPermission',
  full_name='GlobalPermission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='GlobalPermission.action', index=0,
      number=1, type=14, cpp_type=8, label=3,
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
  serialized_start=540,
  serialized_end=594,
)


_USERPERMISSION = _descriptor.Descriptor(
  name='UserPermission',
  full_name='UserPermission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='UserPermission.user', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permission', full_name='UserPermission.permission', index=1,
      number=3, type=11, cpp_type=10, label=2,
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
  serialized_start=596,
  serialized_end=659,
)


_USERSANDPERMISSIONS_USERPERMISSIONS = _descriptor.Descriptor(
  name='UserPermissions',
  full_name='UsersAndPermissions.UserPermissions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='UsersAndPermissions.UserPermissions.user', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='UsersAndPermissions.UserPermissions.permissions', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=749,
  serialized_end=814,
)

_USERSANDPERMISSIONS = _descriptor.Descriptor(
  name='UsersAndPermissions',
  full_name='UsersAndPermissions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_permissions', full_name='UsersAndPermissions.user_permissions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_USERSANDPERMISSIONS_USERPERMISSIONS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=662,
  serialized_end=814,
)


_GRANTREQUEST = _descriptor.Descriptor(
  name='GrantRequest',
  full_name='GrantRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_permission', full_name='GrantRequest.user_permission', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  serialized_start=816,
  serialized_end=872,
)


_GRANTRESPONSE = _descriptor.Descriptor(
  name='GrantResponse',
  full_name='GrantResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=874,
  serialized_end=889,
)


_REVOKEREQUEST = _descriptor.Descriptor(
  name='RevokeRequest',
  full_name='RevokeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_permission', full_name='RevokeRequest.user_permission', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  serialized_start=891,
  serialized_end=948,
)


_REVOKERESPONSE = _descriptor.Descriptor(
  name='RevokeResponse',
  full_name='RevokeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=950,
  serialized_end=966,
)


_GETUSERPERMISSIONSREQUEST = _descriptor.Descriptor(
  name='GetUserPermissionsRequest',
  full_name='GetUserPermissionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='GetUserPermissionsRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table_name', full_name='GetUserPermissionsRequest.table_name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namespace_name', full_name='GetUserPermissionsRequest.namespace_name', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=968,
  serialized_end=1083,
)


_GETUSERPERMISSIONSRESPONSE = _descriptor.Descriptor(
  name='GetUserPermissionsResponse',
  full_name='GetUserPermissionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_permission', full_name='GetUserPermissionsResponse.user_permission', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=1085,
  serialized_end=1155,
)


_CHECKPERMISSIONSREQUEST = _descriptor.Descriptor(
  name='CheckPermissionsRequest',
  full_name='CheckPermissionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='permission', full_name='CheckPermissionsRequest.permission', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=1157,
  serialized_end=1215,
)


_CHECKPERMISSIONSRESPONSE = _descriptor.Descriptor(
  name='CheckPermissionsResponse',
  full_name='CheckPermissionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1217,
  serialized_end=1243,
)

_PERMISSION.fields_by_name['type'].enum_type = _PERMISSION_TYPE
_PERMISSION.fields_by_name['global_permission'].message_type = _GLOBALPERMISSION
_PERMISSION.fields_by_name['namespace_permission'].message_type = _NAMESPACEPERMISSION
_PERMISSION.fields_by_name['table_permission'].message_type = _TABLEPERMISSION
_PERMISSION_ACTION.containing_type = _PERMISSION
_PERMISSION_TYPE.containing_type = _PERMISSION
_TABLEPERMISSION.fields_by_name['table_name'].message_type = HBase__pb2._TABLENAME
_TABLEPERMISSION.fields_by_name['action'].enum_type = _PERMISSION_ACTION
_NAMESPACEPERMISSION.fields_by_name['action'].enum_type = _PERMISSION_ACTION
_GLOBALPERMISSION.fields_by_name['action'].enum_type = _PERMISSION_ACTION
_USERPERMISSION.fields_by_name['permission'].message_type = _PERMISSION
_USERSANDPERMISSIONS_USERPERMISSIONS.fields_by_name['permissions'].message_type = _PERMISSION
_USERSANDPERMISSIONS_USERPERMISSIONS.containing_type = _USERSANDPERMISSIONS
_USERSANDPERMISSIONS.fields_by_name['user_permissions'].message_type = _USERSANDPERMISSIONS_USERPERMISSIONS
_GRANTREQUEST.fields_by_name['user_permission'].message_type = _USERPERMISSION
_REVOKEREQUEST.fields_by_name['user_permission'].message_type = _USERPERMISSION
_GETUSERPERMISSIONSREQUEST.fields_by_name['type'].enum_type = _PERMISSION_TYPE
_GETUSERPERMISSIONSREQUEST.fields_by_name['table_name'].message_type = HBase__pb2._TABLENAME
_GETUSERPERMISSIONSRESPONSE.fields_by_name['user_permission'].message_type = _USERPERMISSION
_CHECKPERMISSIONSREQUEST.fields_by_name['permission'].message_type = _PERMISSION
DESCRIPTOR.message_types_by_name['Permission'] = _PERMISSION
DESCRIPTOR.message_types_by_name['TablePermission'] = _TABLEPERMISSION
DESCRIPTOR.message_types_by_name['NamespacePermission'] = _NAMESPACEPERMISSION
DESCRIPTOR.message_types_by_name['GlobalPermission'] = _GLOBALPERMISSION
DESCRIPTOR.message_types_by_name['UserPermission'] = _USERPERMISSION
DESCRIPTOR.message_types_by_name['UsersAndPermissions'] = _USERSANDPERMISSIONS
DESCRIPTOR.message_types_by_name['GrantRequest'] = _GRANTREQUEST
DESCRIPTOR.message_types_by_name['GrantResponse'] = _GRANTRESPONSE
DESCRIPTOR.message_types_by_name['RevokeRequest'] = _REVOKEREQUEST
DESCRIPTOR.message_types_by_name['RevokeResponse'] = _REVOKERESPONSE
DESCRIPTOR.message_types_by_name['GetUserPermissionsRequest'] = _GETUSERPERMISSIONSREQUEST
DESCRIPTOR.message_types_by_name['GetUserPermissionsResponse'] = _GETUSERPERMISSIONSRESPONSE
DESCRIPTOR.message_types_by_name['CheckPermissionsRequest'] = _CHECKPERMISSIONSREQUEST
DESCRIPTOR.message_types_by_name['CheckPermissionsResponse'] = _CHECKPERMISSIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Permission = _reflection.GeneratedProtocolMessageType('Permission', (_message.Message,), dict(
  DESCRIPTOR = _PERMISSION,
  __module__ = 'AccessControl_pb2'
  # @@protoc_insertion_point(class_scope:Permission)
  ))
_sym_db.RegisterMessage(Permission)

TablePermission = _reflection.GeneratedProtocolMessageType('TablePermission', (_message.Message,), dict(
  DESCRIPTOR = _TABLEPERMISSION,
  __module__ = 'AccessControl_pb2'
  # @@protoc_insertion_point(class_scope:TablePermission)
  ))
_sym_db.RegisterMessage(TablePermission)

NamespacePermission = _reflection.GeneratedProtocolMessageType('NamespacePermission', (_message.Message,), dict(
  DESCRIPTOR = _NAMESPACEPERMISSION,
  __module__ = 'AccessControl_pb2'
  # @@protoc_insertion_point(class_scope:NamespacePermission)
  ))
_sym_db.RegisterMessage(NamespacePermission)

GlobalPermission = _reflection.GeneratedProtocolMessageType('GlobalPermission', (_message.Message,), dict(
  DESCRIPTOR = _GLOBALPERMISSION,
  __module__ = 'AccessControl_pb2'
  # @@protoc_insertion_point(class_scope:GlobalPermission)
  ))
_sym_db.RegisterMessage(GlobalPermission)

UserPermission = _reflection.GeneratedProtocolMessageType('UserPermission', (_message.Message,), dict(
  DESCRIPTOR = _USERPERMISSION,
  __module__ = 'AccessControl_pb2'
  # @@protoc_insertion_point(class_scope:UserPermission)
  ))
_sym_db.RegisterMessage(UserPermission)

UsersAndPermissions = _reflection.GeneratedProtocolMessageType('UsersAndPermissions', (_message.Message,), dict(

  UserPermissions = _reflection.GeneratedProtocolMessageType('UserPermissions', (_message.Message,), dict(
    DESCRIPTOR = _USERSANDPERMISSIONS_USERPERMISSIONS,
    __module__ = 'AccessControl_pb2'
    # @@protoc_insertion_point(class_scope:UsersAndPermissions.UserPermissions)
    ))
  ,
  DESCRIPTOR = _USERSANDPERMISSIONS,
  __module__ = 'AccessControl_pb2'
  # @@protoc_insertion_point(class_scope:UsersAndPermissions)
  ))
_sym_db.RegisterMessage(UsersAndPermissions)
_sym_db.RegisterMessage(UsersAndPermissions.UserPermissions)

GrantRequest = _reflection.GeneratedProtocolMessageType('GrantRequest', (_message.Message,), dict(
  DESCRIPTOR = _GRANTREQUEST,
  __module__ = 'AccessControl_pb2'
  # @@protoc_insertion_point(class_scope:GrantRequest)
  ))
_sym_db.RegisterMessage(GrantRequest)

GrantResponse = _reflection.GeneratedProtocolMessageType('GrantResponse', (_message.Message,), dict(
  DESCRIPTOR = _GRANTRESPONSE,
  __module__ = 'AccessControl_pb2'
  # @@protoc_insertion_point(class_scope:GrantResponse)
  ))
_sym_db.RegisterMessage(GrantResponse)

RevokeRequest = _reflection.GeneratedProtocolMessageType('RevokeRequest', (_message.Message,), dict(
  DESCRIPTOR = _REVOKEREQUEST,
  __module__ = 'AccessControl_pb2'
  # @@protoc_insertion_point(class_scope:RevokeRequest)
  ))
_sym_db.RegisterMessage(RevokeRequest)

RevokeResponse = _reflection.GeneratedProtocolMessageType('RevokeResponse', (_message.Message,), dict(
  DESCRIPTOR = _REVOKERESPONSE,
  __module__ = 'AccessControl_pb2'
  # @@protoc_insertion_point(class_scope:RevokeResponse)
  ))
_sym_db.RegisterMessage(RevokeResponse)

GetUserPermissionsRequest = _reflection.GeneratedProtocolMessageType('GetUserPermissionsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETUSERPERMISSIONSREQUEST,
  __module__ = 'AccessControl_pb2'
  # @@protoc_insertion_point(class_scope:GetUserPermissionsRequest)
  ))
_sym_db.RegisterMessage(GetUserPermissionsRequest)

GetUserPermissionsResponse = _reflection.GeneratedProtocolMessageType('GetUserPermissionsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETUSERPERMISSIONSRESPONSE,
  __module__ = 'AccessControl_pb2'
  # @@protoc_insertion_point(class_scope:GetUserPermissionsResponse)
  ))
_sym_db.RegisterMessage(GetUserPermissionsResponse)

CheckPermissionsRequest = _reflection.GeneratedProtocolMessageType('CheckPermissionsRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHECKPERMISSIONSREQUEST,
  __module__ = 'AccessControl_pb2'
  # @@protoc_insertion_point(class_scope:CheckPermissionsRequest)
  ))
_sym_db.RegisterMessage(CheckPermissionsRequest)

CheckPermissionsResponse = _reflection.GeneratedProtocolMessageType('CheckPermissionsResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHECKPERMISSIONSRESPONSE,
  __module__ = 'AccessControl_pb2'
  # @@protoc_insertion_point(class_scope:CheckPermissionsResponse)
  ))
_sym_db.RegisterMessage(CheckPermissionsResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n*org.apache.hadoop.hbase.protobuf.generatedB\023AccessControlProtosH\001\210\001\001\240\001\001'))

_ACCESSCONTROLSERVICE = _descriptor.ServiceDescriptor(
  name='AccessControlService',
  full_name='AccessControlService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1246,
  serialized_end=1503,
  methods=[
  _descriptor.MethodDescriptor(
    name='Grant',
    full_name='AccessControlService.Grant',
    index=0,
    containing_service=None,
    input_type=_GRANTREQUEST,
    output_type=_GRANTRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Revoke',
    full_name='AccessControlService.Revoke',
    index=1,
    containing_service=None,
    input_type=_REVOKEREQUEST,
    output_type=_REVOKERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetUserPermissions',
    full_name='AccessControlService.GetUserPermissions',
    index=2,
    containing_service=None,
    input_type=_GETUSERPERMISSIONSREQUEST,
    output_type=_GETUSERPERMISSIONSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CheckPermissions',
    full_name='AccessControlService.CheckPermissions',
    index=3,
    containing_service=None,
    input_type=_CHECKPERMISSIONSREQUEST,
    output_type=_CHECKPERMISSIONSRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACCESSCONTROLSERVICE)

DESCRIPTOR.services_by_name['AccessControlService'] = _ACCESSCONTROLSERVICE

# @@protoc_insertion_point(module_scope)
