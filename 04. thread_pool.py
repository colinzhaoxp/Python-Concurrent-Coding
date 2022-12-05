import concurrent.futures
import blog_spider

# craw
# 线程池的第一个用法，需要提前准备好参数
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.craw, blog_spider.urls)
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print('craw: ', url, len(html))
    print('craw over')

# 线程池的第二种用法，参数一个一个的进入就行
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url

    # 按照创建的顺序返回结果
    # for future, url in futures.items():
    #     print('parse: ', url, len(future.result()))

    # 按照完成的顺序返回结果
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url, len(future.result()))

