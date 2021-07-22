package(default_visibility = ["PUBLIC"])

subinclude("//build/please:python.plz")


ge_python_library(
  name="registry-api",
  deps=[
    "//build/thirdparty/gepython:grpc-stubs",

    "//oaas/oaas",
  ],
  srcs=glob(["oaas_registry_api/**/*.py"]),
)
