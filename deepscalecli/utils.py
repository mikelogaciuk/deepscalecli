from timeit import default_timer as timer
from functools import wraps
import base64


def chronometer(func):
    """
    Decorator that processes task computation time and returns its function name.

    :param func: A func that has to be wrapped
    :return: Computation time with a task name.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):

        starting_time = timer()
        task_name: str = str(func.__name__).replace('_', ' ').capitalize()
        result = func(*args, **kwargs)
        ending_time = timer()

        print(f"Task: '{task_name}', has been processed in: {(ending_time - starting_time): 0.4f} seconds.")

        return result
    return wrapper


def encode_key(key: str) -> str:
    """
    Encodes message to base64.

    :param key: A phrase to encode
    :return: base64 string
    """
    message_bytes = key.encode("ascii")
    encode_value = base64.b64encode(message_bytes)
    message = encode_value.decode("ascii")

    return message


def decode_key(key: str) -> str:
    """
    Decodes message from base64 to string.

    :param key: A base64 key to decode.
    :return: string
    """
    base64_bytes = key.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')

    return message

