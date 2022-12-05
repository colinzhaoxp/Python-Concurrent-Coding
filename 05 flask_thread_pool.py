import json
import time
import flask
from concurrent.futures import ThreadPoolExecutor

app = flask.Flask(__name__)
pool = ThreadPoolExecutor() # 放在方法里面会有问题

def read_file():
    time.sleep(0.1)
    return 'file result'


def read_db():
    time.sleep(0.2)
    return 'file db'


def read_api():
    time.sleep(0.3)
    return 'file api'


@app.route('/')
def index():
    result_file = pool.submit(read_file)
    result_db = pool.submit(read_db)
    result_api = pool.submit(read_api)

    return json.dumps({
        'result_file': result_file.result(),
        'result_db': result_db.result(),
        'result_api': result_api.result(),
    })

if __name__ == "__main__":
    app.run()