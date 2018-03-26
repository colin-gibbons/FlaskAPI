from flask import Flask, render_template, jsonify
import hashlib
import math

app = Flask(__name__)

tasks = [ # add your tasks here
    {
        'id':'md5',
        'title': "MD5",
        'description': 'Return md5 hash.',
        'done':False
    },
    {
        'id':'factorial',
        'title': 'Factorial',
        'description': 'Return n factorial.',
        'done':False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/')
def index():
    return render_template('index.html', output="Try /md5/message to see its md5 hash.")

@app.route('/md5/<string>')
def getMD5(string): # TODO: needs to return correct http status codes
    md5Hash = hashlib.sha224(str(string).encode('utf-8')).hexdigest()
    return render_template('index.html', output=md5Hash)

@app.route('/factorial/<string>')  # TODO: needs to return correct http status codes
def getFactorial(string):
    factorial = math.factorial(int(string))
    return render_template('index.html', output=factorial)

if __name__ == "__main__":
    app.run(host="0.0.0.0")



