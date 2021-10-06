#!/usr/bin/python3
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/healthcheck", methods=['GET'])
def health_api():
  msg = {"code": 200, "msg": "ok"}

  return jsonify(msg), 200

@app.route('/v1/mock', methods=['GET'])
def mock_api():
  msg = {"code": 200, "guid": "abcd1234"}

  return jsonify(msg), 200

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
