from flask import Flask, jsonify

app = Flask(__name__)



@app.route("/hello")
def hello():
    return jsonify("hello"), 200

@app.route("/suma/<a>/<b>")
def suma(a, b):
    return jsonify(int(a)+int(b)), 200


if __name__ == "__main__":
    app.run(debug=True)