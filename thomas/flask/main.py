from flask import *
import time

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<givenname>')
def hello(name="a name",givenname="a givenname"):
    return render_template('hello.html',name=name, givenname=givenname)

@app.route('/result')
def renderResult():
    result = request.args.get('input')
    return render_template('result.html',result=result)

app.run(debug=True)
