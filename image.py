import flask
from flask import Flask, request, Response, jsonify

app = Flask(__name__)

print(flask.__version__)

@app.route('/api/myimages', methods=['POST'])
def myimages():
    req = request

    if req == None:
        print('The request is null')
    else:
        print(req.data)
    response = {"values": req.data}

    return jsonify(values=response)


@app.route('/api/users', methods=['GET'])
def users():
    req = request

    users = {
        "name": "Kuda"
    }

    return jsonify(users=users)


app.run(host="localhost", port=5015)
