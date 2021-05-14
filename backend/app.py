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
    parser = argparse.ArgumentParser()
    parser.add_argument('-test', help='test the compilation of the application')
    parser.add_argument('-host', help='host address')
    parser.add_argument('-port', help='host port number')
    args = parser.parse_args()

    if args.test:
        print("Successfully compiled")
        sys.exit(0)

    app.run(debug=True, host=args.host, port=args.port)