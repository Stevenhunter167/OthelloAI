from flask import Flask, request, render_template
from config import PORTNUMBER
from Global import data
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('canvasplot.html')

@app.route('/consoleout')
def console_data_in():
    message = request.args.get('message')
    data['console'].append(message)
    return ''

@app.route('/dataout')
def data_out():
    return json.dumps(data)

@app.route('/start/')
def start():
    import main
    return "started"


if __name__ == '__main__':
    app.run('localhost', PORTNUMBER, debug=True)