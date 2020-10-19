from flask import *
import db.dbconnect as Database
from datetime import datetime
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/init_database')
def initDB():

    status = Database.Database().init()

    return render_template('db_created.html', result=status)


@app.route('/')
def capital():
    return render_template('define_endpoint.html')

@app.route('/<path:path>', methods=['GET', 'POST'])
def mock(path):

    # look up the db for path
    # return json response by asking db with path and query

    query = request.args

    #return render_template('mock_result.html', request=path, query=query, response="{a json response}")

    return {
        "username" : "g.user.username",
        "e-mail" : "g.user.email"
    }

    return jsonify(
        username="g.user.username",
        email="g.user.email"
    )

@app.route('/addMockEndpoint', methods=['POST'])
def addMockEndpoint():
    
    if request.method == 'POST':
        formdata= request.form

        EP_flavor = formdata['flavor']
        EP_description = formdata['description']
        EP_method = formdata['method']
        EP_path = formdata['request']
        parts = urlparse(EP_path)
        EP_json = formdata['response']

        # current date and time
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        Database.Database().addResponseForPath(EP_description, EP_flavor, EP_method, EP_path, EP_json)

        text = "date_time: {0} flavor: {1}; description: {2}; method: {3}; request: {4}; response: {5}".format(date_time, EP_flavor, EP_description, EP_method, parts, EP_json)

        return render_template('result.html',country=input, result=text)

    else :

        return render_template('result.html',country=input, result="not saved")

app.run(debug=True)
