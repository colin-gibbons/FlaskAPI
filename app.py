from flask import Flask, render_template, jsonify, abort, make_response, request
from urllib import request as urlRequest
from urllib import parse
from slackclient import SlackClient
import hashlib
import math
import json
import redis

app = Flask(__name__)
redis_ip = '35.231.14.95'
redis_port = 6379

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
    },
    {
        'id':'kv-record',
        'title': 'kv-record',
        'description': 'Records posted k/v pair to REDIS database.',
        'done':True
    },
    {
        'id':'kv-retrieve',
        'title': 'kv-retrieve',
        'description': 'Retrieves key value from REDIS database. ',
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
    md5Hash = hashlib.md5(str(string).encode('utf-8')).hexdigest()
    return jsonify({'input':string, 'output':md5Hash})

@app.route('/is-prime/<int:x>', methods=['GET']) # Prime
def getprime(x):
    if x == 1:
        return jsonify({'input':x, 'output':False})

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
    req = urlRequest.Request("https://hooks.slack.com/services/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", data = json_post.encode('ascii'), headers = {'Content-Type': 'application/json'})
    urlRequest.urlopen(req)
    return jsonify({'input':string, 'output':True})

@app.route('/kv-retrieve/<string:string>', methods=['GET']) # kv retrieve
def retrieve(string):
    r = redis.StrictRedis(host=redis_ip, port=redis_port, db=0)
    out = r.get(string)
    error = 'none'

    if type(out) == bytes:
        out = out.decode("utf-8")
    else:
        out = False
        error = 'Key does not exist.'

    return jsonify({'input':string, 'output':out, 'error': error})

@app.route('/kv-record', methods=['POST', 'PUT']) # kv record
def record():
    data = request.form
    r = redis.StrictRedis(host=redis_ip, port=redis_port, db=0)
    error = 'none'
    if request.method == 'POST':
        for key, value in data.items():
            if not r.exists(key):
                r.set(key, value)
                print("Adding new k/v pair: (" + key + ", " + value +")")
            else:
                error = 'Unable to add pair: Key already exists.'
                return jsonify({'input':data, 'output':False, 'error': error})
    elif request.method == 'PUT':
        for key, value in data.items():
            if r.exists(key):
                r.set(key, value)
                print("Updating k/v pair: (" + key + ", " + value +")")
            else:
                error = 'Unable to update pair: Key does not exist.'
                return jsonify({'input':data, 'output':False, 'error': error})
    return jsonify({'input':data, 'output':True, 'error': error})

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


