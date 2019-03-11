import os

from flask import Flask, flash, render_template, request, redirect
from config import APPKEY

app = Flask(__name__)
app.debug = True
app.secret_key = APPKEY

from config import db

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    debug = True
    if 'DYNO' in os.environ:
        debug = False
        print('debug mode OFF')
    else:
        print('>>> debug mode ON')
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=debug)
