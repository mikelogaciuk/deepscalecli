from timeit import default_timer as timer
from functools import wraps
import random
import string
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


def generate_key(size: int = 18):
    """
    Generates a random key with a specific size.
    :param size:
    :return:
    """
    val: str = ""

    for i in range(size):
        val += random.choice(string.ascii_letters)
        for key in range(1):
            val += str(random.randint(0, size))

    return val