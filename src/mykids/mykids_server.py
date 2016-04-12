import argparse

from flask import Flask, jsonify
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


@app.route('/get/albums', methods=['GET'])
def get_albums():
    response = []
    for i in range(1, 10, 1):
        response.append({"name": "album" + str(i), "id": i})
    return jsonify({'albums': response})


@app.route('/get/album/<int:album_id>', methods=['GET'])
def get_album_by_id(album_id):
    response = []
    for i in range(1, 10, 1):
        response.append({"name": "album" + str(i), "id": i})
    return jsonify({'albums': response})


def parse_args():
    parser = argparse.ArgumentParser(description='Mykids Server')
    parser.add_argument('-d', '--debug', help='Debug')
    parser.add_argument('-p', '--port', help='Port', type=int, default=8000)
    return vars(parser.parse_args())


if __name__ == '__main__':
    args = parse_args()
    app_options = {"port": int(args["port"]), "host": "0.0.0.0"}

    if args["debug"]:
        app_options["debug"] = True
        app_options["use_debugger"] = False
        app_options["use_reloader"] = False
    else:
        app_options["threaded"] = True

    app.run(**app_options)
