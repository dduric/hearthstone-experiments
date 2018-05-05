import sys, os
sys.path.append(os.getcwd())

from hslog.liveparser import LiveLogParser
from flask import Flask, request

liveParser = LiveLogParser(None)

app = Flask(__name__)


@app.route("/", methods=['POST'])
def hello():
    req_data = request.get_json()

    # feed the parser
    liveParser.flask_endpoint(req_data['line'].strip())
    return ''

if __name__ == '__main__':
    app.run(debug=True, port=5000)