package(default_visibility = ["PUBLIC"])

subinclude("//build/please:python.plz")


python_library(
  name="registry-api-lib",
  srcs=glob([
    "oaas_registry_api/**/*.py",
  ]),
  deps=[
    "//build/thirdparty/python:grpc-stubs",

    "//oaas/oaas:oaas-lib",
  ],
)


ge_python_library(
  name="registry-api",
  deps=[
    "//build/thirdparty/gepython:grpc-stubs",

    "//oaas/oaas",
  ],
  srcs=glob(["oaas_registry_api/**/*.py"]),
)
