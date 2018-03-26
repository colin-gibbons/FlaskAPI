from flask import Flask, render_template
import hashlib
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', output="Try /md5/message to see its md5 hash.")

@app.route('/md5/<string>')
def getMD5(string):
    md5Hash = hashlib.sha224(str(string).encode('utf-8')).hexdigest()
    return render_template('index.html', output=md5Hash)

@app.route('/factorial/<string>')
def getFactorial(string):
    factorial = math.factorial(int(string))
    return render_template('index.html', output=factorial)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
