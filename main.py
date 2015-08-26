__author__ = 'chenjensen'
from flask import Flask,render_template,request
from namepaire import namePaire
from scrubxz import xzSrcub
from scrub_blood import bloodScrub
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('base.html')

#Fate test by name
@app.route('/name',methods=['POST','GET'])
def delname():
    if request.method == 'POST':
        ndHelper = namePaire()
        return render_template('nametest.html',list=ndHelper.getresult(request.form['man'].encode('gbk'),request.form['woman'].encode('gbk')),man=request.form['man'],woman=request.form['woman'])
    else:
        return render_template('nametest.html')

#Fate test by Constellation
@app.route('/xz',methods=['POST','GET'])
def delxz():
    if request.method == 'POST':
        xzHlper = xzSrcub()
        return render_template('xztest.html',list=xzHlper.getresult(request.form['man'],request.form['woman']))
    else:
        return render_template('xztest.html')

#Fate test by Blood
@app.route('/xx',methods=['POST','GET'])
def delxx():
    if request.method == 'POST':
        xxhlper = bloodScrub()
        return render_template('xxtest.html',list = xxhlper.getResult(request.form['man'],request.form['woman']))
    else:
        return render_template('xxtest.html')

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0')