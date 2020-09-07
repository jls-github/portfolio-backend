from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        "route": "/"
    })


@app.route('/projects')
def projects():
    return jsonify({
        "route": "/projects"
    })

