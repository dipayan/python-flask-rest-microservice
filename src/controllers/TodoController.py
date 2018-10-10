#/src/controllers/TodoController.py
from flask import request, g, Blueprint, json, Response
from ..models.TodoModel import TodoModel, TodoSchema

todo_api = Blueprint('todo_api', __name__)
todo_schema = TodoSchema()


@todo_api.route('/', methods=['POST'])
def create():
  """
  Create a Todo Function
  """
  req_data = request.get_json()
  data, error = todo_schema.load(req_data)
  if error:
    return custom_response(error, 400)
  post = TodoModel(data)
  post.save()
  data = todo_schema.dump(post).data
  return custom_response(data, 201)

@todo_api.route('/', methods=['GET'])
def get_all():
  """
  Get All Todos
  """
  posts = TodoModel.get_all_todos()
  data = todo_schema.dump(posts, many=True).data
  return custom_response(data, 200)

@todo_api.route('/<int:todo_id>', methods=['GET'])
def get_one(todo_id):
  """
  Get A Todo
  """
  post = TodoModel.get_one_todo(todo_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = todo_schema.dump(post).data
  return custom_response(data, 200)

@todo_api.route('/<int:todo_id>', methods=['PUT'])
def update(todo_id):
  """
  Update A Todo
  """
  req_data = request.get_json()
  post = TodoModel.get_one_todo(todo_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = todo_schema.dump(post).data

  data, error = todo_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)
  post.update(data)
  
  data = todo_schema.dump(post).data
  return custom_response(data, 200)

@todo_api.route('/<int:todo_id>', methods=['DELETE'])
def delete(todo_id):
  """
  Delete A Todo
  """
  post = TodoModel.get_one_todo(todo_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = todo_schema.dump(post).data

  post.delete()
  return custom_response({'message': 'deleted'}, 204)
  

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )

