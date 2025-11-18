
"""
Debezium encodes decimal values as  {scale: scale, value: "base64 value"}
"""
import base64


def decode_decimal(obj) -> int:
    if isinstance(obj, dict):
        return int.from_bytes(base64.b64decode(obj['value']), 'big') / pow(10, obj['scale'])
    # If already a string or int, just convert to int
    return int(obj)