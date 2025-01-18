import base64

def b64_decode(base64_string):
    base64_bytes = base64_string.encode('utf-8')
    byte_string = base64.b64decode(base64_bytes)
    original_string = byte_string.decode('utf-8')

    return original_string

def b64_encode(original_string):
    byte_string = original_string.encode('utf-8')
    base64_bytes = base64.b64encode(byte_string)
    base64_string = base64_bytes.decode('utf-8')

    return base64_string
