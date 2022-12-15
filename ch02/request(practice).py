#----------practice start------------
from flask import Flask, request
#----------practice end--------------

app = Flask(__name__)

#----------practice start------------
@app.route('/')
def url_is():
    url_ = request.url
    return f'<h1>Link is "{url_}"!</h1>'
#----------practice end--------------

if __name__ == '__main__':
    app.run(debug=True)


