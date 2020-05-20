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
    response = {"image": req.data}
    # response_pickled = jsonpickle.encode(response)
    message = {
        "value": "Kuda"
    }

    return jsonify(msg=req.data)


@app.route('/api/users', methods=['GET'])
def users():
    req = request

    users = {
        "name": "Kuda"
    }

    return jsonify(users=users)


app.run(host="localhost", port=5015)
