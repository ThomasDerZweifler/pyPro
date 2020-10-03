from flask import *
import db.dbconnect as Database
import time

app = Flask(__name__)

@app.route('/')
def capital():
    return render_template('hello.html')

@app.route('/result')
def renderResult():
    input = request.args.get('input')

    result = Database.Database().getCapital(input)

    return render_template('result.html',country=input, result=result)

app.run(debug=True)
