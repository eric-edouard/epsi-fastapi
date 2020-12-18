from flask import Flask, request, jsonify, abort

app = Flask(__name__)

todos = [
    {
        "id": 0,
        "task": "Faire les courses",
        "isDone": False,
    },
    {
        "id": 1,
        "task": "Apprendre le JS",
        "isDone": False,
    },
]

@app.route('/todo/', methods=['GET'])
def get_todo_details():
    id = int(request.args.get("id")) # check if number is correct before converting to int
    print(f'Searching for todo with id {id}')
    for todo in todos:
        if todo["id"] == id:
            return jsonify(todo)
    abort(404)

@app.route('/todo/', methods=['POST'])
def check_todo():
    id = int(request.args.get("id"))
    isDone = request.args.get("id") # check if number is correct before converting to int
    if (isDone == "false"):
        isDone = False
    else:
        isDone = True
    print(f'Setting todo with id {id} at {isDone}')

    for todo in todos:
        if todo["id"] == id:
            todo["isDone"] = isDone
            return jsonify(todo)
    abort(404)


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
    id = len(todos)
    todos.append({
        "id": id,
        "task": todo,
        "isDone": False
    })
    return jsonify(todos)




if __name__ == '__main__':
    app.run(threaded=True, port=5000)
