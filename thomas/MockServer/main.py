from flask import *
import db.dbconnect as Database
from datetime import datetime
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/')
def capital():
    return render_template('define_endpoint.html')

@app.route('/<path:path>', methods=['GET', 'POST'])
def mock(path):

    # look up the db for path
    # return json response by asking db with path and query

    query = request.args

    return render_template('mock_result.html', request=path, query=query, response="{a json response}")

@app.route('/addMockEndpoint', methods=['POST'])
def addMockEndpoint():
    
    if request.method == 'POST':
        formdata= request.form

        method = formdata['method']
        req = formdata['request']
        parts = urlparse(req)
        res = formdata['response']

        # current date and time
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    # save to db    
     #result = Database.Database().getCapital(input)

        text = "date_time: {0} method: {1}; request: {2}; response: {3}".format(date_time, method, parts, res)

        return render_template('result.html',country=input, result=text)

    else :

        return render_template('result.html',country=input, result="not saved")

app.run(debug=True)
