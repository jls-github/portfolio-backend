from flask import Flask, jsonify
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        "route": "/"
    })


@app.route('/projects/<project_id>')
def projects_show(project_id):
    return jsonify({
        "route": '/projects/%s' % escape(project_id)
    })

@app.route('/projects')
def projects():
    return jsonify({
        "route": "/projects"
    })

