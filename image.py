import base64
from typing import BinaryIO

from flask import Flask, request, Response, jsonify

app = Flask(__name__)


@app.route('/api/myimages', methods=['POST'])
def myimages():
    req = request

    if req == None:
        print('The request is null')
    else:
        print(req.data)

    # image_decode = base64.decodebytes(req.data)
    # print(type(image_decode))
    # with open('me.png', 'wb') as dimage:
    #     dimage.write(image_decode)

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
