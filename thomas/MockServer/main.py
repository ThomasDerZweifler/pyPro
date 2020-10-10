from flask import *
import db.dbconnect as Database
import time

app = Flask(__name__)

@app.route('/')
def capital():
    return render_template('hello.html')

@app.route('/mock/<path:path>', methods=['GET', 'POST'])
def mock(path):

    # return json response by asking db with path and query

    query = request.args

    return render_template('mock_result.html', request=path, query=query, response="{a json response}")

@app.route('/addMockEndpoint', methods=['POST'])
def addMockEndpoint():
    
    if request.method == 'POST':
        formdata= request.form

        method = formdata['method']
        req = formdata['request']
        res = formdata['response']

    # save to db    
     #result = Database.Database().getCapital(input)

        text = "method: {0}; request: {1}; response: {2}".format(method, req, res)

        return render_template('result.html',country=input, result=text)

    else :

        return render_template('result.html',country=input, result="not saved")

app.run(debug=True)
