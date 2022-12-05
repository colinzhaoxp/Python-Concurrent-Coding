import time

import blog_spider
import threading

def single_thread():
    print('single_thread start')
    for url in blog_spider.urls:
        blog_spider.craw(url)
    print('single_thread end')

def multi_thread():
    print('multi_thread start')
    threads = []
    for url in blog_spider.urls:
        threads.append(
            threading.Thread(target=blog_spider.craw, args=(url,))
        )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print('multi_thread end')

if __name__ == '__main__':
    start = time.time()
    single_thread()
    print(f'single_thread: {time.time() - start}')
    start = time.time()
    multi_thread()
    print(f'multi_thread: {time.time() - start}')
