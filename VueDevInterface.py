import os
from flask import Flask,request,make_response,jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
import redis
import json
import pymongo

# redis
r=redis.StrictRedis(host='localhost',port=6379)
# mongo
mongo=pymongo.MongoClient('mongodb://localhost:27017/')

app = Flask(__name__)
CORS(app,supports_credentials=True)

@app.route('/Login',methods=["Post"])
def Login():
    data=json.loads(request.data)
    if data is not None:
        # 将用户数据进行存储
        if r.get(data['username']):
            return make_response("成功")
    return make_response("失败")

@app.route('/Upload',methods=['Post','Get'])
def Upload():
    upload_file=request.files['file']
    if upload_file and allowed_file(upload_file.filename):
        filename=secure_filename(upload_file.filename)
        # 将文件保存到 static/uploads 目录，文件名同上传时使用的文件名
        upload_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
        return 'info is ' + request.form.get('info', '') + '. success'
    else:
        return 'failed'

# 文件上传目录
app.config['UPLOAD_FOLDER'] = 'static\\uploads\\'
# 支持的文件格式
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}  # 集合类型
# 判断文件名是否是我们支持的格式
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/Goods',methods=['Post','Get'])
def Goods():
    # mongo Goods数据库 Books表
    goods=mongo['Goods']
    books=goods['Books']
    res=[x for x in books.find({},{"_id":0})]
    return jsonify(res);



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)