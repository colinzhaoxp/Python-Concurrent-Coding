import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

PRIMES = [13213546515413] * 50

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    sqrt_n = int(math.floor(math.sqrt(number)))
    for i in range(3, sqrt_n+1, 2):
        if number % i == 0:
            return False
    return True

def single_thread():
    for number in PRIMES:
        is_prime(number)

def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)

def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)

if __name__ == '__main__':
    start = time.time()
    single_thread()
    print('time:', time.time() - start)
    start = time.time()
    multi_thread()
    print('time: ', time.time() - start)
    start = time.time()
    multi_process()
    print('time: ', time.time() - start)


