def parm_type_int(int_value):
    if int_value.isdigit():
        return True
    return False

def parm_type_str(str_value):
    if isinstance(str_value, str):
        return True
    return False

def parm_type_bool(bool_value):
    if isinstance(bool_value, bool):
        return True
    return False
