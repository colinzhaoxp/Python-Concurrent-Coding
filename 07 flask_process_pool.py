import json
import math

import flask
from concurrent.futures import ProcessPoolExecutor

app = flask.Flask(__name__)


# pool = ProcessPoolExecutor() 放这里会报错

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    sqrt_n = int(math.floor(math.sqrt(number)))
    for i in range(3, sqrt_n + 1, 2):
        if number % i == 0:
            return False
    return True


@app.route('/is_prime/<numbers>')
def api_is_prime(numbers):
    number_list = [int(x) for x in numbers.split(',')]
    print(number_list)
    results = pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, results)))


if __name__ == "__main__":
    # 当使用pool的时候，他所依赖的函数声明必须已经申明完成了
    # pool要放在main函数下才能配合flask使用
    pool = ProcessPoolExecutor()
    app.run()
