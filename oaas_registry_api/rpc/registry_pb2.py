# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: registry.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="registry.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0eregistry.proto"\xc5\x01\n\x15OaasServiceDefinition\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12.\n\x04tags\x18\x04 \x03(\x0b\x32 .OaasServiceDefinition.TagsEntry\x12\x11\n\tlocations\x18\x05 \x03(\t\x12\n\n\x02id\x18\x06 \x01(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x1b\n\rOaasServiceId\x12\n\n\x02id\x18\x01 \x01(\t"F\n\x1aOaasResolveServiceResponse\x12(\n\x08services\x18\x01 \x03(\x0b\x32\x16.OaasServiceDefinition"/\n\x1dOaasUnregisterServiceResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x32\xe0\x01\n\x0cOaasRegistry\x12\x42\n\x10register_service\x12\x16.OaasServiceDefinition\x1a\x16.OaasServiceDefinition\x12\x46\n\x0fresolve_service\x12\x16.OaasServiceDefinition\x1a\x1b.OaasResolveServiceResponse\x12\x44\n\x12unregister_service\x12\x0e.OaasServiceId\x1a\x1e.OaasUnregisterServiceResponseb\x06proto3',
)


_OAASSERVICEDEFINITION_TAGSENTRY = _descriptor.Descriptor(
    name="TagsEntry",
    full_name="OaasServiceDefinition.TagsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="OaasServiceDefinition.TagsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="OaasServiceDefinition.TagsEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=173,
    serialized_end=216,
)

_OAASSERVICEDEFINITION = _descriptor.Descriptor(
    name="OaasServiceDefinition",
    full_name="OaasServiceDefinition",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="namespace",
            full_name="OaasServiceDefinition.namespace",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="name",
            full_name="OaasServiceDefinition.name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="version",
            full_name="OaasServiceDefinition.version",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="tags",
            full_name="OaasServiceDefinition.tags",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="locations",
            full_name="OaasServiceDefinition.locations",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="id",
            full_name="OaasServiceDefinition.id",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[
        _OAASSERVICEDEFINITION_TAGSENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=19,
    serialized_end=216,
)


_OAASSERVICEID = _descriptor.Descriptor(
    name="OaasServiceId",
    full_name="OaasServiceId",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="OaasServiceId.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=218,
    serialized_end=245,
)


_OAASRESOLVESERVICERESPONSE = _descriptor.Descriptor(
    name="OaasResolveServiceResponse",
    full_name="OaasResolveServiceResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="services",
            full_name="OaasResolveServiceResponse.services",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=247,
    serialized_end=317,
)


_OAASUNREGISTERSERVICERESPONSE = _descriptor.Descriptor(
    name="OaasUnregisterServiceResponse",
    full_name="OaasUnregisterServiceResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="result",
            full_name="OaasUnregisterServiceResponse.result",
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=319,
    serialized_end=366,
)

_OAASSERVICEDEFINITION_TAGSENTRY.containing_type = _OAASSERVICEDEFINITION
_OAASSERVICEDEFINITION.fields_by_name[
    "tags"
].message_type = _OAASSERVICEDEFINITION_TAGSENTRY
_OAASRESOLVESERVICERESPONSE.fields_by_name[
    "services"
].message_type = _OAASSERVICEDEFINITION
DESCRIPTOR.message_types_by_name["OaasServiceDefinition"] = _OAASSERVICEDEFINITION
DESCRIPTOR.message_types_by_name["OaasServiceId"] = _OAASSERVICEID
DESCRIPTOR.message_types_by_name[
    "OaasResolveServiceResponse"
] = _OAASRESOLVESERVICERESPONSE
DESCRIPTOR.message_types_by_name[
    "OaasUnregisterServiceResponse"
] = _OAASUNREGISTERSERVICERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OaasServiceDefinition = _reflection.GeneratedProtocolMessageType(
    "OaasServiceDefinition",
    (_message.Message,),
    {
        "TagsEntry": _reflection.GeneratedProtocolMessageType(
            "TagsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _OAASSERVICEDEFINITION_TAGSENTRY,
                "__module__": "registry_pb2"
                # @@protoc_insertion_point(class_scope:OaasServiceDefinition.TagsEntry)
            },
        ),
        "DESCRIPTOR": _OAASSERVICEDEFINITION,
        "__module__": "registry_pb2"
        # @@protoc_insertion_point(class_scope:OaasServiceDefinition)
    },
)
_sym_db.RegisterMessage(OaasServiceDefinition)
_sym_db.RegisterMessage(OaasServiceDefinition.TagsEntry)

OaasServiceId = _reflection.GeneratedProtocolMessageType(
    "OaasServiceId",
    (_message.Message,),
    {
        "DESCRIPTOR": _OAASSERVICEID,
        "__module__": "registry_pb2"
        # @@protoc_insertion_point(class_scope:OaasServiceId)
    },
)
_sym_db.RegisterMessage(OaasServiceId)

OaasResolveServiceResponse = _reflection.GeneratedProtocolMessageType(
    "OaasResolveServiceResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _OAASRESOLVESERVICERESPONSE,
        "__module__": "registry_pb2"
        # @@protoc_insertion_point(class_scope:OaasResolveServiceResponse)
    },
)
_sym_db.RegisterMessage(OaasResolveServiceResponse)

OaasUnregisterServiceResponse = _reflection.GeneratedProtocolMessageType(
    "OaasUnregisterServiceResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _OAASUNREGISTERSERVICERESPONSE,
        "__module__": "registry_pb2"
        # @@protoc_insertion_point(class_scope:OaasUnregisterServiceResponse)
    },
)
_sym_db.RegisterMessage(OaasUnregisterServiceResponse)


_OAASSERVICEDEFINITION_TAGSENTRY._options = None

_OAASREGISTRY = _descriptor.ServiceDescriptor(
    name="OaasRegistry",
    full_name="OaasRegistry",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=369,
    serialized_end=593,
    methods=[
        _descriptor.MethodDescriptor(
            name="register_service",
            full_name="OaasRegistry.register_service",
            index=0,
            containing_service=None,
            input_type=_OAASSERVICEDEFINITION,
            output_type=_OAASSERVICEDEFINITION,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="resolve_service",
            full_name="OaasRegistry.resolve_service",
            index=1,
            containing_service=None,
            input_type=_OAASSERVICEDEFINITION,
            output_type=_OAASRESOLVESERVICERESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="unregister_service",
            full_name="OaasRegistry.unregister_service",
            index=2,
            containing_service=None,
            input_type=_OAASSERVICEID,
            output_type=_OAASUNREGISTERSERVICERESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_OAASREGISTRY)

DESCRIPTOR.services_by_name["OaasRegistry"] = _OAASREGISTRY

# @@protoc_insertion_point(module_scope)
