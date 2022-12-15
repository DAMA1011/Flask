from flask import Flask, render_template, request
from flask_moment import Moment
from datetime import datetime


# practice start
from pathlib import Path
import uuid
# practice end

app = Flask(__name__)
moment = Moment(app)

# practice start
# 創建資料夾: 依照目前檔案 Path(__file__) 的路徑，透過解析 .resolve()，選擇此路徑的父目錄 (ch08)，建立子目錄 (uploaded)
UPLOAD_FOLDER = Path(__file__).resolve().parent/'uploaded'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
# practice end

@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header",
                           current_time=datetime.utcnow())


# practice start
@app.route('/file', methods=['GET', 'POST'])
def get_file():
    if request.method == "GET":
        return render_template('file(practice).html', page_header="upload file")
    elif request.method == "POST":
        file = request.files['file123'] # key is the value of name(html attribute) in <input type="file">
        if file:
            filename = str(uuid.uuid4())+"_"+file.filename
            file.save(UPLOAD_FOLDER/filename)
        data = [["method:", request.method],
                ["base_url:", request.base_url],
                ["file:",request.files]]
        return render_template('form_result(practice).html', page_header="review file", data=data)
# practice end


if __name__ == "__main__":
    app.run(debug=True)
