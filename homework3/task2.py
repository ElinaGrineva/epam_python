# Here's a not very efficient calculation function that calculates something important:
#
# import time
# import struct
# import random
# import hashlib
# from timeit import timeit
#
# def slow_calculate(value):
#     """Some weird voodoo magic calculations"""
#     time.sleep(random.randint(1,3))
#     data = hashlib.md5(str(value).encode()).digest()
#     return sum(struct.unpack('<' + 'B' * len(data), data))
# # Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
# # Calculation time should not take more than a minute. Use functional capabilities of multiprocessing module.
# # You are not allowed to modify slow_calculate function.


import hashlib
import random
import struct
import time
from multiprocessing import Pool


# flake8: noqa: S311,S303
def slow_calculate(value: int) -> int:
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def multiprocessing__calculate(func=slow_calculate) -> int:
    with Pool(50) as p:
        res = p.map(func, list(range(501)))
        p.close()
        p.join()
    return sum(res)
