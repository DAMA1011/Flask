from flask import Flask, render_template


app = Flask(__name__)



#----------practice start------------
@app.route('/')
def index():
    return render_template("basic_extends(practice).html", page_header = "Page header", x=10)

@app.route('/block')
def block():
    return render_template("block(practice).html")

@app.route('/super')
def jinja2_super():
    return render_template("super(practice).html", page_header = "test super()")
#----------practice end-------------- 


if __name__=="__main__":
    app.run(debug=True)
