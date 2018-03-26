from flask import Flask, render_template, jsonify, abort, make_response
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

@app.errorhandler(404) # handles 404 errors
def notFound(error):
    return make_response(jsonify({'404 error': 'Page not found.'}), 404)

@app.route('/tasks', methods=['GET']) # returns list of tasks
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/<str:taskID>', methods=['GET']) # checks to see if task exists before calling it
def getTask(taskID):
    task = [task for task in tasks if task['id'] == taskID]
    if len(task) == 0:
        abort(404)
    return jsonify({'task':task[0]})

@app.route('/md5/<str:string>')
def getMD5(string):
    md5Hash = hashlib.sha224(str(string).encode('utf-8')).hexdigest()
    return render_template('index.html', output=md5Hash)

@app.route('/factorial/<int:x>')
def getFactorial(x):
    factorial = math.factorial(int(x))
    return render_template('index.html', output=factorial)

if __name__ == "__main__":
    app.run(host="0.0.0.0")



