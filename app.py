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
    return jsonify({'input':string, 'output':True})

@app.route('/fibonacci/<int:x>', methods=['GET']) # Fibonacci
def fibonacci(x):
    if x >= 0:
        a = 0
        b = 1
        fibArray = [a,b]
        
        while b <= x:
            a,b = b, a+b
            fibArray.append(b)
        
        fibArray = fibArray[:-1]
    else:
        b = "Please choose a number greater than 0"
        fibArray = []
        fibArray.append(b)
    return jsonify({'input':x, 'output':fibArray})

# Added 400 Error for bad input
@app.route('/fibonacci/<string:inStr>', methods=['GET'])
def fibErr(inStr):
    return make_response(jsonify({'error': '400: Bad Request - Invalid Input'}), 400)
@app.route('/factorial/<string:inStr>', methods=['GET'])
def factErr(inStr):
    return make_response(jsonify({'error': '400: Bad Request - Invalid Input'}), 400)
@app.route('/is-prime/<string:inStr>', methods=['GET'])
def primeErr(inStr):
    return make_response(jsonify({'error': '400: Bad Request - Invalid Input'}), 400)

if __name__ == "__main__":
    app.run(host="0.0.0.0") 


