from flask import Blueprint, jsonify

todo_bp = Blueprint('todo', __name__)

todos_list = [
    {'id': 1, 'task': 'Buy groceries', 'completed': False},
    {'id': 2, 'task': 'Clean the house', 'completed': True},
    {'id': 3, 'task': 'Finish homework', 'completed': False}
]
@todo_bp.route('/todo', methods=['GET'])
def get_todos():
    return jsonify(todos_list)
  