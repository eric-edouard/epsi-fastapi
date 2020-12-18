from flask import Flask, request, jsonify

app = Flask(__name__)

todos = ["Faire les courses", "apprendre python"]


@app.route('/')
def index():
    return "<h1>Welcome to our server !</h1>"


@app.route('/todos')
def get_todos():
    return jsonify(todos)

@app.route('/todo/', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    print(f'Adding ${todo} to the list...')
    todos.append(todo)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
