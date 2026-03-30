from flask import Blueprint, jsonify, request
from uuid import uuid4

todo_bp = Blueprint('todo', __name__)

todos_list = [
    {'id': 1, 'task': 'Buy groceries', 'completed': False},
    {'id': 2, 'task': 'Clean the house', 'completed': True},
    {'id': 3, 'task': 'Finish homework', 'completed': False}
]
@todo_bp.route('/todo', methods=['GET'])
def get_todos():
    return jsonify(todos_list, uuid4())
  
@todo_bp.route('/todo/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((todo for todo in todos_list if todo['id'] == todo_id), None)
    if todo:
        return jsonify(todo, )
    else:
        return jsonify({'error': 'Todo not found'}), 404
@todo_bp.route('/todo', methods=['POST'])
def create_todo():
    request_data = request.get_json()
    new_todo = {
        'id': uuid4(),
        'task': request_data.get('task'),
        'completed': request_data.get('completed')
    }
    todos_list.append(new_todo)
    return jsonify(new_todo), 201