__author__ = 'chenjensen'
from flask import Flask,render_template,request
from scrubxz import xzSrcub
from namepaire import namePaire
app = Flask(__name__)
@app.route('/',methods=['POST', 'GET'])
def showHome():
    if request.method=='POST':
        scruber = xzSrcub()
        list = scruber.getresult(request.form['man'],request.form['woman'])
        return render_template('agetest.html',list=list)
    else:
        list=''
        return render_template('agetest.html',list=list)
@app.route('/name',methods=['POST', 'GET'])
def showName():
    if request.method=='POST':
        nametest = namePaire()
        list = nametest.getresult(request.form['man'],request.form['woman'])
        return render_template('nametest.html',list=list)
    else:
        list=''
        return render_template('nametest.html',list=list)
@app.route('/test')
def getresult():
    scruber = xzSrcub()
    list = scruber.getresult()
    return render_template('agetest.html',list=list)
if __name__=='__main__':
    app.debug= True
    app.run(host='0.0.0.0')
