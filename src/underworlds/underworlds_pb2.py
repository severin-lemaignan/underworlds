# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: underworlds.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='underworlds.proto',
  package='underworlds',
  syntax='proto3',
  serialized_pb=_b('\n\x11underworlds.proto\x12\x0bunderworlds\"\x14\n\x06\x43lient\x12\n\n\x02id\x18\x01 \x01(\t\"\xa5\x01\n\x04Node\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12#\n\x04type\x18\x03 \x01(\x0e\x32\x15.underworlds.NodeType\x12\x0e\n\x06parent\x18\x04 \x01(\t\x12\x10\n\x08\x63hildren\x18\x05 \x03(\t\x12\x16\n\x0etransformation\x18\x06 \x03(\x02\x12\x13\n\x0blast_update\x18\x08 \x01(\x02\x12\x0f\n\x07physics\x18\x10 \x01(\x08\"\x14\n\x05Nodes\x12\x0b\n\x03ids\x18\x01 \x03(\t\"(\n\x07\x43ontext\x12\x0e\n\x06\x63lient\x18\x01 \x01(\t\x12\r\n\x05world\x18\x02 \x01(\t\"\x14\n\x04Name\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x14\n\x04Size\x12\x0c\n\x04size\x18\x01 \x01(\x05\"W\n\rNodeInContext\x12%\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x14.underworlds.Context\x12\x1f\n\x04node\x18\x02 \x01(\x0b\x32\x11.underworlds.Node\"O\n\x10NodeInvalidation\x12/\n\x04type\x18\x01 \x01(\x0e\x32!.underworlds.NodeInvalidationType\x12\n\n\x02id\x18\x02 \x01(\t\"\x14\n\x04Time\x12\x0c\n\x04time\x18\x01 \x01(\x02\"W\n\x14TimelineInvalidation\x12\x33\n\x04type\x18\x01 \x01(\x0e\x32%.underworlds.TimelineInvalidationType\x12\n\n\x02id\x18\x02 \x01(\t\"\x07\n\x05\x45mpty*;\n\x08NodeType\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06\x45NTITY\x10\x01\x12\x08\n\x04MESH\x10\x02\x12\n\n\x06\x43\x41MERA\x10\x03*7\n\x14NodeInvalidationType\x12\x07\n\x03NEW\x10\x00\x12\n\n\x06UPDATE\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02*9\n\x18TimelineInvalidationType\x12\t\n\x05\x45VENT\x10\x00\x12\t\n\x05START\x10\x01\x12\x07\n\x03\x45ND\x10\x02\x32\x91\x05\n\x0bUnderworlds\x12\x30\n\x04helo\x12\x11.underworlds.Name\x1a\x13.underworlds.Client\"\x00\x12\x38\n\x0bgetNodesLen\x12\x14.underworlds.Context\x1a\x11.underworlds.Size\"\x00\x12\x39\n\x0bgetNodesIds\x12\x14.underworlds.Context\x1a\x12.underworlds.Nodes\"\x00\x12\x38\n\x0bgetRootNode\x12\x14.underworlds.Context\x1a\x11.underworlds.Node\"\x00\x12:\n\x07getNode\x12\x1a.underworlds.NodeInContext\x1a\x11.underworlds.Node\"\x00\x12>\n\nupdateNode\x12\x1a.underworlds.NodeInContext\x1a\x12.underworlds.Empty\"\x00\x12>\n\ndeleteNode\x12\x1a.underworlds.NodeInContext\x1a\x12.underworlds.Empty\"\x00\x12O\n\x14getNodeInvalidations\x12\x14.underworlds.Context\x1a\x1d.underworlds.NodeInvalidation\"\x00\x30\x01\x12;\n\x0etimelineOrigin\x12\x14.underworlds.Context\x1a\x11.underworlds.Time\"\x00\x12W\n\x18getTimelineInvalidations\x12\x14.underworlds.Context\x1a!.underworlds.TimelineInvalidation\"\x00\x30\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_NODETYPE = _descriptor.EnumDescriptor(
  name='NodeType',
  full_name='underworlds.NodeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENTITY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESH', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMERA', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=622,
  serialized_end=681,
)
_sym_db.RegisterEnumDescriptor(_NODETYPE)

NodeType = enum_type_wrapper.EnumTypeWrapper(_NODETYPE)
_NODEINVALIDATIONTYPE = _descriptor.EnumDescriptor(
  name='NodeInvalidationType',
  full_name='underworlds.NodeInvalidationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NEW', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=683,
  serialized_end=738,
)
_sym_db.RegisterEnumDescriptor(_NODEINVALIDATIONTYPE)

NodeInvalidationType = enum_type_wrapper.EnumTypeWrapper(_NODEINVALIDATIONTYPE)
_TIMELINEINVALIDATIONTYPE = _descriptor.EnumDescriptor(
  name='TimelineInvalidationType',
  full_name='underworlds.TimelineInvalidationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EVENT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=740,
  serialized_end=797,
)
_sym_db.RegisterEnumDescriptor(_TIMELINEINVALIDATIONTYPE)

TimelineInvalidationType = enum_type_wrapper.EnumTypeWrapper(_TIMELINEINVALIDATIONTYPE)
UNDEFINED = 0
ENTITY = 1
MESH = 2
CAMERA = 3
NEW = 0
UPDATE = 1
DELETE = 2
EVENT = 0
START = 1
END = 2



_CLIENT = _descriptor.Descriptor(
  name='Client',
  full_name='underworlds.Client',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='underworlds.Client.id', index=0,
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
  serialized_start=34,
  serialized_end=54,
)


_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='underworlds.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='underworlds.Node.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='underworlds.Node.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='underworlds.Node.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent', full_name='underworlds.Node.parent', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='children', full_name='underworlds.Node.children', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transformation', full_name='underworlds.Node.transformation', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_update', full_name='underworlds.Node.last_update', index=6,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='physics', full_name='underworlds.Node.physics', index=7,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=57,
  serialized_end=222,
)


_NODES = _descriptor.Descriptor(
  name='Nodes',
  full_name='underworlds.Nodes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='underworlds.Nodes.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=224,
  serialized_end=244,
)


_CONTEXT = _descriptor.Descriptor(
  name='Context',
  full_name='underworlds.Context',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client', full_name='underworlds.Context.client', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='world', full_name='underworlds.Context.world', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=246,
  serialized_end=286,
)


_NAME = _descriptor.Descriptor(
  name='Name',
  full_name='underworlds.Name',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='underworlds.Name.name', index=0,
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
  serialized_start=288,
  serialized_end=308,
)


_SIZE = _descriptor.Descriptor(
  name='Size',
  full_name='underworlds.Size',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='underworlds.Size.size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=310,
  serialized_end=330,
)


_NODEINCONTEXT = _descriptor.Descriptor(
  name='NodeInContext',
  full_name='underworlds.NodeInContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='underworlds.NodeInContext.context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node', full_name='underworlds.NodeInContext.node', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=332,
  serialized_end=419,
)


_NODEINVALIDATION = _descriptor.Descriptor(
  name='NodeInvalidation',
  full_name='underworlds.NodeInvalidation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='underworlds.NodeInvalidation.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='underworlds.NodeInvalidation.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=421,
  serialized_end=500,
)


_TIME = _descriptor.Descriptor(
  name='Time',
  full_name='underworlds.Time',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='underworlds.Time.time', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=502,
  serialized_end=522,
)


_TIMELINEINVALIDATION = _descriptor.Descriptor(
  name='TimelineInvalidation',
  full_name='underworlds.TimelineInvalidation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='underworlds.TimelineInvalidation.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='underworlds.TimelineInvalidation.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=524,
  serialized_end=611,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='underworlds.Empty',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=613,
  serialized_end=620,
)

_NODE.fields_by_name['type'].enum_type = _NODETYPE
_NODEINCONTEXT.fields_by_name['context'].message_type = _CONTEXT
_NODEINCONTEXT.fields_by_name['node'].message_type = _NODE
_NODEINVALIDATION.fields_by_name['type'].enum_type = _NODEINVALIDATIONTYPE
_TIMELINEINVALIDATION.fields_by_name['type'].enum_type = _TIMELINEINVALIDATIONTYPE
DESCRIPTOR.message_types_by_name['Client'] = _CLIENT
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Nodes'] = _NODES
DESCRIPTOR.message_types_by_name['Context'] = _CONTEXT
DESCRIPTOR.message_types_by_name['Name'] = _NAME
DESCRIPTOR.message_types_by_name['Size'] = _SIZE
DESCRIPTOR.message_types_by_name['NodeInContext'] = _NODEINCONTEXT
DESCRIPTOR.message_types_by_name['NodeInvalidation'] = _NODEINVALIDATION
DESCRIPTOR.message_types_by_name['Time'] = _TIME
DESCRIPTOR.message_types_by_name['TimelineInvalidation'] = _TIMELINEINVALIDATION
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.enum_types_by_name['NodeType'] = _NODETYPE
DESCRIPTOR.enum_types_by_name['NodeInvalidationType'] = _NODEINVALIDATIONTYPE
DESCRIPTOR.enum_types_by_name['TimelineInvalidationType'] = _TIMELINEINVALIDATIONTYPE

Client = _reflection.GeneratedProtocolMessageType('Client', (_message.Message,), dict(
  DESCRIPTOR = _CLIENT,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.Client)
  ))
_sym_db.RegisterMessage(Client)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), dict(
  DESCRIPTOR = _NODE,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.Node)
  ))
_sym_db.RegisterMessage(Node)

Nodes = _reflection.GeneratedProtocolMessageType('Nodes', (_message.Message,), dict(
  DESCRIPTOR = _NODES,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.Nodes)
  ))
_sym_db.RegisterMessage(Nodes)

Context = _reflection.GeneratedProtocolMessageType('Context', (_message.Message,), dict(
  DESCRIPTOR = _CONTEXT,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.Context)
  ))
_sym_db.RegisterMessage(Context)

Name = _reflection.GeneratedProtocolMessageType('Name', (_message.Message,), dict(
  DESCRIPTOR = _NAME,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.Name)
  ))
_sym_db.RegisterMessage(Name)

Size = _reflection.GeneratedProtocolMessageType('Size', (_message.Message,), dict(
  DESCRIPTOR = _SIZE,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.Size)
  ))
_sym_db.RegisterMessage(Size)

NodeInContext = _reflection.GeneratedProtocolMessageType('NodeInContext', (_message.Message,), dict(
  DESCRIPTOR = _NODEINCONTEXT,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.NodeInContext)
  ))
_sym_db.RegisterMessage(NodeInContext)

NodeInvalidation = _reflection.GeneratedProtocolMessageType('NodeInvalidation', (_message.Message,), dict(
  DESCRIPTOR = _NODEINVALIDATION,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.NodeInvalidation)
  ))
_sym_db.RegisterMessage(NodeInvalidation)

Time = _reflection.GeneratedProtocolMessageType('Time', (_message.Message,), dict(
  DESCRIPTOR = _TIME,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.Time)
  ))
_sym_db.RegisterMessage(Time)

TimelineInvalidation = _reflection.GeneratedProtocolMessageType('TimelineInvalidation', (_message.Message,), dict(
  DESCRIPTOR = _TIMELINEINVALIDATION,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.TimelineInvalidation)
  ))
_sym_db.RegisterMessage(TimelineInvalidation)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'underworlds_pb2'
  # @@protoc_insertion_point(class_scope:underworlds.Empty)
  ))
_sym_db.RegisterMessage(Empty)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class UnderworldsStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.helo = channel.unary_unary(
        '/underworlds.Underworlds/helo',
        request_serializer=Name.SerializeToString,
        response_deserializer=Client.FromString,
        )
    self.getNodesLen = channel.unary_unary(
        '/underworlds.Underworlds/getNodesLen',
        request_serializer=Context.SerializeToString,
        response_deserializer=Size.FromString,
        )
    self.getNodesIds = channel.unary_unary(
        '/underworlds.Underworlds/getNodesIds',
        request_serializer=Context.SerializeToString,
        response_deserializer=Nodes.FromString,
        )
    self.getRootNode = channel.unary_unary(
        '/underworlds.Underworlds/getRootNode',
        request_serializer=Context.SerializeToString,
        response_deserializer=Node.FromString,
        )
    self.getNode = channel.unary_unary(
        '/underworlds.Underworlds/getNode',
        request_serializer=NodeInContext.SerializeToString,
        response_deserializer=Node.FromString,
        )
    self.updateNode = channel.unary_unary(
        '/underworlds.Underworlds/updateNode',
        request_serializer=NodeInContext.SerializeToString,
        response_deserializer=Empty.FromString,
        )
    self.deleteNode = channel.unary_unary(
        '/underworlds.Underworlds/deleteNode',
        request_serializer=NodeInContext.SerializeToString,
        response_deserializer=Empty.FromString,
        )
    self.getNodeInvalidations = channel.unary_stream(
        '/underworlds.Underworlds/getNodeInvalidations',
        request_serializer=Context.SerializeToString,
        response_deserializer=NodeInvalidation.FromString,
        )
    self.timelineOrigin = channel.unary_unary(
        '/underworlds.Underworlds/timelineOrigin',
        request_serializer=Context.SerializeToString,
        response_deserializer=Time.FromString,
        )
    self.getTimelineInvalidations = channel.unary_stream(
        '/underworlds.Underworlds/getTimelineInvalidations',
        request_serializer=Context.SerializeToString,
        response_deserializer=TimelineInvalidation.FromString,
        )


class UnderworldsServicer(object):

  def helo(self, request, context):
    """Establish the connection to the server, setting a human-friendly name for
    the client.
    The server returns a unique client ID that must be used in every subsequent
    request to the server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getNodesLen(self, request, context):
    """NODES

    Returns the number of nodes in a given world.

    Accepts a context (client ID and world) and returns the number of existing nodes.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getNodesIds(self, request, context):
    """Returns the list of node IDs present in the given world
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getRootNode(self, request, context):
    """Returns the root node ID of the given world
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getNode(self, request, context):
    """Returns a node from its ID in the given world.
    Note that only the node ID is used (and thus, required).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateNode(self, request, context):
    """Updates (and broadcasts to all client) a node in a given world
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteNode(self, request, context):
    """Deletes (and broadcasts to all client) a node in a given world
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getNodeInvalidations(self, request, context):
    """Returns a (stream of) 'invalidated' nodes that need to be updated.
    Invalidated nodes can be new nodes, nodes that have changed, or nodes
    that have been removed (see Invalidation.type).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def timelineOrigin(self, request, context):
    """TIMELINE

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getTimelineInvalidations(self, request, context):
    """Returns a (stream of) 'invalidated' nodes that need to be updated.
    Invalidated nodes can be new nodes, nodes that have changed, or nodes
    that have been removed (see Invalidation.type).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UnderworldsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'helo': grpc.unary_unary_rpc_method_handler(
          servicer.helo,
          request_deserializer=Name.FromString,
          response_serializer=Client.SerializeToString,
      ),
      'getNodesLen': grpc.unary_unary_rpc_method_handler(
          servicer.getNodesLen,
          request_deserializer=Context.FromString,
          response_serializer=Size.SerializeToString,
      ),
      'getNodesIds': grpc.unary_unary_rpc_method_handler(
          servicer.getNodesIds,
          request_deserializer=Context.FromString,
          response_serializer=Nodes.SerializeToString,
      ),
      'getRootNode': grpc.unary_unary_rpc_method_handler(
          servicer.getRootNode,
          request_deserializer=Context.FromString,
          response_serializer=Node.SerializeToString,
      ),
      'getNode': grpc.unary_unary_rpc_method_handler(
          servicer.getNode,
          request_deserializer=NodeInContext.FromString,
          response_serializer=Node.SerializeToString,
      ),
      'updateNode': grpc.unary_unary_rpc_method_handler(
          servicer.updateNode,
          request_deserializer=NodeInContext.FromString,
          response_serializer=Empty.SerializeToString,
      ),
      'deleteNode': grpc.unary_unary_rpc_method_handler(
          servicer.deleteNode,
          request_deserializer=NodeInContext.FromString,
          response_serializer=Empty.SerializeToString,
      ),
      'getNodeInvalidations': grpc.unary_stream_rpc_method_handler(
          servicer.getNodeInvalidations,
          request_deserializer=Context.FromString,
          response_serializer=NodeInvalidation.SerializeToString,
      ),
      'timelineOrigin': grpc.unary_unary_rpc_method_handler(
          servicer.timelineOrigin,
          request_deserializer=Context.FromString,
          response_serializer=Time.SerializeToString,
      ),
      'getTimelineInvalidations': grpc.unary_stream_rpc_method_handler(
          servicer.getTimelineInvalidations,
          request_deserializer=Context.FromString,
          response_serializer=TimelineInvalidation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'underworlds.Underworlds', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaUnderworldsServicer(object):
  def helo(self, request, context):
    """Establish the connection to the server, setting a human-friendly name for
    the client.
    The server returns a unique client ID that must be used in every subsequent
    request to the server.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def getNodesLen(self, request, context):
    """NODES

    Returns the number of nodes in a given world.

    Accepts a context (client ID and world) and returns the number of existing nodes.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def getNodesIds(self, request, context):
    """Returns the list of node IDs present in the given world
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def getRootNode(self, request, context):
    """Returns the root node ID of the given world
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def getNode(self, request, context):
    """Returns a node from its ID in the given world.
    Note that only the node ID is used (and thus, required).
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def updateNode(self, request, context):
    """Updates (and broadcasts to all client) a node in a given world
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def deleteNode(self, request, context):
    """Deletes (and broadcasts to all client) a node in a given world
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def getNodeInvalidations(self, request, context):
    """Returns a (stream of) 'invalidated' nodes that need to be updated.
    Invalidated nodes can be new nodes, nodes that have changed, or nodes
    that have been removed (see Invalidation.type).
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def timelineOrigin(self, request, context):
    """TIMELINE

    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def getTimelineInvalidations(self, request, context):
    """Returns a (stream of) 'invalidated' nodes that need to be updated.
    Invalidated nodes can be new nodes, nodes that have changed, or nodes
    that have been removed (see Invalidation.type).
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaUnderworldsStub(object):
  def helo(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Establish the connection to the server, setting a human-friendly name for
    the client.
    The server returns a unique client ID that must be used in every subsequent
    request to the server.
    """
    raise NotImplementedError()
  helo.future = None
  def getNodesLen(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """NODES

    Returns the number of nodes in a given world.

    Accepts a context (client ID and world) and returns the number of existing nodes.
    """
    raise NotImplementedError()
  getNodesLen.future = None
  def getNodesIds(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Returns the list of node IDs present in the given world
    """
    raise NotImplementedError()
  getNodesIds.future = None
  def getRootNode(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Returns the root node ID of the given world
    """
    raise NotImplementedError()
  getRootNode.future = None
  def getNode(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Returns a node from its ID in the given world.
    Note that only the node ID is used (and thus, required).
    """
    raise NotImplementedError()
  getNode.future = None
  def updateNode(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Updates (and broadcasts to all client) a node in a given world
    """
    raise NotImplementedError()
  updateNode.future = None
  def deleteNode(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Deletes (and broadcasts to all client) a node in a given world
    """
    raise NotImplementedError()
  deleteNode.future = None
  def getNodeInvalidations(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Returns a (stream of) 'invalidated' nodes that need to be updated.
    Invalidated nodes can be new nodes, nodes that have changed, or nodes
    that have been removed (see Invalidation.type).
    """
    raise NotImplementedError()
  def timelineOrigin(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """TIMELINE

    """
    raise NotImplementedError()
  timelineOrigin.future = None
  def getTimelineInvalidations(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Returns a (stream of) 'invalidated' nodes that need to be updated.
    Invalidated nodes can be new nodes, nodes that have changed, or nodes
    that have been removed (see Invalidation.type).
    """
    raise NotImplementedError()


def beta_create_Underworlds_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('underworlds.Underworlds', 'deleteNode'): NodeInContext.FromString,
    ('underworlds.Underworlds', 'getNode'): NodeInContext.FromString,
    ('underworlds.Underworlds', 'getNodeInvalidations'): Context.FromString,
    ('underworlds.Underworlds', 'getNodesIds'): Context.FromString,
    ('underworlds.Underworlds', 'getNodesLen'): Context.FromString,
    ('underworlds.Underworlds', 'getRootNode'): Context.FromString,
    ('underworlds.Underworlds', 'getTimelineInvalidations'): Context.FromString,
    ('underworlds.Underworlds', 'helo'): Name.FromString,
    ('underworlds.Underworlds', 'timelineOrigin'): Context.FromString,
    ('underworlds.Underworlds', 'updateNode'): NodeInContext.FromString,
  }
  response_serializers = {
    ('underworlds.Underworlds', 'deleteNode'): Empty.SerializeToString,
    ('underworlds.Underworlds', 'getNode'): Node.SerializeToString,
    ('underworlds.Underworlds', 'getNodeInvalidations'): NodeInvalidation.SerializeToString,
    ('underworlds.Underworlds', 'getNodesIds'): Nodes.SerializeToString,
    ('underworlds.Underworlds', 'getNodesLen'): Size.SerializeToString,
    ('underworlds.Underworlds', 'getRootNode'): Node.SerializeToString,
    ('underworlds.Underworlds', 'getTimelineInvalidations'): TimelineInvalidation.SerializeToString,
    ('underworlds.Underworlds', 'helo'): Client.SerializeToString,
    ('underworlds.Underworlds', 'timelineOrigin'): Time.SerializeToString,
    ('underworlds.Underworlds', 'updateNode'): Empty.SerializeToString,
  }
  method_implementations = {
    ('underworlds.Underworlds', 'deleteNode'): face_utilities.unary_unary_inline(servicer.deleteNode),
    ('underworlds.Underworlds', 'getNode'): face_utilities.unary_unary_inline(servicer.getNode),
    ('underworlds.Underworlds', 'getNodeInvalidations'): face_utilities.unary_stream_inline(servicer.getNodeInvalidations),
    ('underworlds.Underworlds', 'getNodesIds'): face_utilities.unary_unary_inline(servicer.getNodesIds),
    ('underworlds.Underworlds', 'getNodesLen'): face_utilities.unary_unary_inline(servicer.getNodesLen),
    ('underworlds.Underworlds', 'getRootNode'): face_utilities.unary_unary_inline(servicer.getRootNode),
    ('underworlds.Underworlds', 'getTimelineInvalidations'): face_utilities.unary_stream_inline(servicer.getTimelineInvalidations),
    ('underworlds.Underworlds', 'helo'): face_utilities.unary_unary_inline(servicer.helo),
    ('underworlds.Underworlds', 'timelineOrigin'): face_utilities.unary_unary_inline(servicer.timelineOrigin),
    ('underworlds.Underworlds', 'updateNode'): face_utilities.unary_unary_inline(servicer.updateNode),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_Underworlds_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('underworlds.Underworlds', 'deleteNode'): NodeInContext.SerializeToString,
    ('underworlds.Underworlds', 'getNode'): NodeInContext.SerializeToString,
    ('underworlds.Underworlds', 'getNodeInvalidations'): Context.SerializeToString,
    ('underworlds.Underworlds', 'getNodesIds'): Context.SerializeToString,
    ('underworlds.Underworlds', 'getNodesLen'): Context.SerializeToString,
    ('underworlds.Underworlds', 'getRootNode'): Context.SerializeToString,
    ('underworlds.Underworlds', 'getTimelineInvalidations'): Context.SerializeToString,
    ('underworlds.Underworlds', 'helo'): Name.SerializeToString,
    ('underworlds.Underworlds', 'timelineOrigin'): Context.SerializeToString,
    ('underworlds.Underworlds', 'updateNode'): NodeInContext.SerializeToString,
  }
  response_deserializers = {
    ('underworlds.Underworlds', 'deleteNode'): Empty.FromString,
    ('underworlds.Underworlds', 'getNode'): Node.FromString,
    ('underworlds.Underworlds', 'getNodeInvalidations'): NodeInvalidation.FromString,
    ('underworlds.Underworlds', 'getNodesIds'): Nodes.FromString,
    ('underworlds.Underworlds', 'getNodesLen'): Size.FromString,
    ('underworlds.Underworlds', 'getRootNode'): Node.FromString,
    ('underworlds.Underworlds', 'getTimelineInvalidations'): TimelineInvalidation.FromString,
    ('underworlds.Underworlds', 'helo'): Client.FromString,
    ('underworlds.Underworlds', 'timelineOrigin'): Time.FromString,
    ('underworlds.Underworlds', 'updateNode'): Empty.FromString,
  }
  cardinalities = {
    'deleteNode': cardinality.Cardinality.UNARY_UNARY,
    'getNode': cardinality.Cardinality.UNARY_UNARY,
    'getNodeInvalidations': cardinality.Cardinality.UNARY_STREAM,
    'getNodesIds': cardinality.Cardinality.UNARY_UNARY,
    'getNodesLen': cardinality.Cardinality.UNARY_UNARY,
    'getRootNode': cardinality.Cardinality.UNARY_UNARY,
    'getTimelineInvalidations': cardinality.Cardinality.UNARY_STREAM,
    'helo': cardinality.Cardinality.UNARY_UNARY,
    'timelineOrigin': cardinality.Cardinality.UNARY_UNARY,
    'updateNode': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'underworlds.Underworlds', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)