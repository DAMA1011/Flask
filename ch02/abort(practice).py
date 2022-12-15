#----------practice start------------
from flask import Flask, abort
#----------practice end--------------

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hi</h1>"

# ----------practice start------------
@app.route('/user/<int:id_>')
def get_user(id_):
    if id_ > 100:
        abort(404)
    return f'<h1>Hello, No.{id_} user</h1>'

# 讓程式掛掉
# @app.route('/user/<int:id_>')
# def get_user1(id_):
#     ans = 100/id_   <-- id 輸入 0
#     if id_ > 100:
#         abort(404)
#     return f'<h1>Hello, No.{id_} user</h1>'
# 要防止程式掛掉，要用 try/except
# ----------practice end--------------


if __name__ == '__main__':
    app.run(debug=True)
