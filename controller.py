from flask import Flask, jsonify, url_for
from markupsafe import escape
app = Flask(__name__)

projects = [
    {"number": 1, "title": "first project"},
    {"number": 2, "title": "second project"},
    {"number": 3, "title": "third project"}
]

@app.route('/')
def hello_world():
    return jsonify({
        "route": "/"
    })


@app.route('/projects/<project_id>')
def projects_show(project_id):
    return jsonify({
        "route": projects[int(project_id)]
    })

@app.route('/projects')
def projects_index():
    return jsonify({
        "route": "/projects"
    })

with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('projects_show', project_id=1))
    print(url_for('projects_index'))
