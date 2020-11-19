from flask import *
from flask_swagger import swagger
import db.dbconnect as Database
from datetime import datetime
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/init_database')
def initDB():
    # use: https://editor.swagger.io/#
    """
        Create a new user
        ---
        tags:
          - users
        definitions:
          - schema:
              id: Group
              properties:
                name:
                 type: string
                 description: the group's name
        parameters:
          - in: body
            name: body
            schema:
              id: User
              required:
                - email
                - name
              properties:
                email:
                  type: string
                  description: email for user
                name:
                  type: string
                  description: name for user
                address:
                  description: address for user
                  schema:
                    id: Address
                    properties:
                      street:
                        type: string
                      state:
                        type: string
                      country:
                        type: string
                      postalcode:
                        type: string
                groups:
                  type: array
                  description: list of groups
                  items:
                    $ref: "#/definitions/Group"
        responses:
          201:
            description: User created
        """
        
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

        success = Database.Database().addResponseForPath(EP_description, EP_flavor, EP_method, EP_path, EP_json)

        text = "date_time: {0} flavor: {1}; description: {2}; method: {3}; request: {4}; response: {5}".format(date_time, EP_flavor, EP_description, EP_method, parts, EP_json)

        succ = "not"

        if(success) :
            succ = "successfully"

        return render_template('result.html', result=text, success=succ)

@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)

app.run(debug=True)
