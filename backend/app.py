# Observatory Service

# Import framework
from flask import Flask
import argparse
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)