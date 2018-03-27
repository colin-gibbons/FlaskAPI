from flask import Flask, render_template, jsonify, abort, make_response
import hashlib
import math
import json
from urllib import request, parse
from slackclient import SlackClient

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
        'description': 'Returns n factorial.',
        'done':False
    },
    {
        'id':'is-prime',
        'title': 'Is Prime',
        'description': 'Returns True if x is prime, otherwise returns False.',
        'done':False
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

if __name__ == "__main__":
    app.run(host="0.0.0.0") 


