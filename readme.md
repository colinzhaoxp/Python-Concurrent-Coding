# python并发学习

## 简介

在编写自己代码的过程中，我已经不止一次注意到当自己的代码运行的时候，
cpu的利用率总是维持在一个不是很高的水平，这让我感觉很奇怪。
后来在深入了解编程之后学习到了并发编程这个概念，一下子就让我之前的疑惑烟消云散了。

鉴于自己现在比较常用python，因此我想以python为基础，来学习一下并发编程的相关知识，以充分压榨cpu的性能。

python并发编程的主要内容包括以下三个方面：多线程、多进程、多协程。
这三个概念之间是存在一定的联系的。

多进程 Process (multiprocessing)：
- 优点：可以利用多核CPU并行运算；
- 缺点：占用资源最多，可启动的数目比较少；
- 适用于：CPU密集型计算

多线程 Thread (Threading)
- 优点：相比进程，更轻量级，占用资源少；
- 缺点：
  - 相比进程：多线程只能并发执行，不能利用多CPU（因为python中GIL的存在）
  - 相比协程：启动数目有限制，占用内存资源，有线程切换开销
- 适用于：IO密集型计算，同时运行的任务数目要求不多

多协程 Coroutine (asyncio)
- 优点：内存开销最少，启动协程的数量最多
- 缺点：支持的库有限制（aiohttp VS requests），代码实现比较复杂；
- 适用于：IO密集型计算，需要超多任务运行，但是有现成库支持的场景

学习用到的资料就会全部放到下面参考资料这个章节中。

## python库
多线程
```python
import threading
p = threading.Thread(target=function_name, args=(arg1,arg2,...))
p.start() # 启动
p.join() # 会阻塞调用这个方法的线程，即p执行完后才会返回这里执行下一句。
```

多进程
```python
from multiprocessing import Process
p = Process(target=function_name, args=(arg1, arg2, ...))
p.start()
p.join()
```

多协程,好像比较复杂，目前来看自己还没有完全理解。 

这一部分还是看08 asyncio_spider.py文件吧
```python
import async # 引入协程需要包
# 定义第一个协程函数
async def foo():
    pass
async def bar():
    await foo() # 表示这一步需要等待的时间比较长
```


## 参考资料
1. bilibili视频【【2021最新版】Python 并发编程实战，用多线程、多进程、多协程加速程序运行】 https://www.bilibili.com/video/BV1bK411A7tV/?p=12&share_source=copy_web&vd_source=3fca6f4036c3f4404c82695266107ac3
2. 