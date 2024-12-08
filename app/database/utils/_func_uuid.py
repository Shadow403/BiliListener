import uuid

def func_generate_uuid(str_value):
    UUID = str(uuid.uuid5(uuid.NAMESPACE_DNS, str_value))
    return UUID
