from app import app
from flask import jsonify, abort

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

######################
## TASKS
######################
## sample data
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

# http://localhost:5000/todo/api/tasks
@app.route('/todo/api/tasks', methods=['GET'])
def get_tasks():

    return jsonify({'tasks': tasks})

# http://localhost:5000/todo/api/tasks/1
@app.route('/todo/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})
