import time
import threading


def my_func(a, b):
    return a + b

def multi_thread(args):
    threads = []
    for a, b in args:
        threads.append(
            threading.Thread(target=my_func, args=(a,b))
        )
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    args = [(i, j) for i, j in enumerate(range(10))]
    start = time.time()
    multi_thread(args)
    print(time.time() - start)