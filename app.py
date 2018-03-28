from flask import Flask, render_template, jsonify, abort, make_response
from urllib import request, parse
from slackclient import SlackClient
import hashlib
import math
import json

app = Flask(__name__)

tasks = [ # list of available API commands
    {
        'id':'md5',
        'title': "MD5",
        'description': 'Returns an md5 hash of the passed string.',
        'done':True
    },
    {
        'id':'factorial',
        'title': 'Factorial',
        'description': 'Returns n factorial.',
        'done':True
    },
    {
        'id':'fibonacci',
        'title': 'Fibonacci',
        'description': 'Returns fibonacci sequence up to n.',
        'done':False
    },
    {
        'id':'is-prime',
        'title': 'Is Prime',
        'description': 'Returns True if n is prime, otherwise returns False.',
        'done':True
    },
    {
        'id':'slack-alert',
        'title': 'Slack Alert',
        'description': 'Prints message to the Group 2 slack channel.',
        'done':True
    }
]

@app.errorhandler(404) # handles 404 errors
def notFound(error):
    return make_response(jsonify({'error': '404: Page not found.'}), 404)

@app.route('/tasks', methods=['GET']) # displays list of available API commands
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/<string:taskID>', methods=['GET'])  # returns info on a specific command
def getTask(taskID):
    task = [task for task in tasks if task['id'] == taskID]
    
    if len(task) == 0:
        abort(404)
    
    return jsonify({'task':task[0]})

@app.route('/md5/<string:string>', methods=['GET']) # MD5
def getMD5(string):
    md5Hash = hashlib.sha224(str(string).encode('utf-8')).hexdigest()
    return jsonify({'input':string, 'output':md5Hash})

@app.route('/is-prime/<int:x>', methods=['GET']) # Prime
def getprime(x):
    for number in range(2,int(x**0.5)+1):
            if x%number==0:
                a = False
                return jsonify({'input':x, 'output':a})
    a = True
    return jsonify({'input':x, 'output':a})

@app.route('/factorial/<int:x>', methods=['GET']) # Factorials
def getFactorial(x):
    factorial = math.factorial(int(x))
    return jsonify({'input':x, 'output':factorial})

@app.route('/slack-alert/<string:string>', methods=['GET']) # Slack-Alert
def slackPost(string):
    post = {"text": "{0}".format(string)}

    json_post = json.dumps(post)
    req = request.Request("https://hooks.slack.com/services/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", data = json_post.encode('ascii'), headers = {'Content-Type': 'application/json'})
    request.urlopen(req)
    return jsonify({'input':string, 'output':("Posted " + string + " to group 2 slack channel.")})

@app.route('/fibonacci/<int:x>', methods=['GET']) # Fibonacci
def fibonacci(x):
    a, b = 0, 1
    while a < x:
        fibonacci = a
        a, b = b, a+b

    return jsonify({'input':x, 'output':fibonacci})

if __name__ == "__main__":
    app.run(host="0.0.0.0") 


