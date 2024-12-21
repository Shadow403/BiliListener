import uuid

def func_generate_uuid(uid, live_timestamp):
    str_value = f"{uid}000{live_timestamp}"
    UUID = str(uuid.uuid5(uuid.NAMESPACE_DNS, str_value))
    return UUID
