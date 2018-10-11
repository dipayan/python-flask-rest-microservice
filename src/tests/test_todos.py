import unittest
import os
import json
from ..app import create_app, db

class TodoTest(unittest.TestCase):
  """
  Todo Test Case
  """
  def setUp(self):
    """
    Test Setup
    """
    self.app = create_app("testing")
    self.client = self.app.test_client
    self.todos = {
      'id': 1,
      'title': 'my first test todo',
      'content': 'I have to create a test case'
    }
    with self.app.app_context():
      # create all tables
      db.create_all()
  
  def test_todo_creation(self):
    """ test todo creation """
    res = self.client().post('/api/v1/todos/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.todos))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 201)

  def test_get_todo(self):
    """ Test Todo Get """
    res = self.client().post('/api/v1/todos/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.todos))
    self.assertEqual(res.status_code, 201)
    json_data = json.loads(res.data)
    res = self.client().get('/api/v1/todos/' + json_data.get('id') , headers={'Content-Type': 'application/json'})
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(json_data.get('title'), 'my first test todo')

  def test_todo_update(self):
    """ Test Update Todo """
    todo1 = {
      'title': 'Update my test case'
    }
    res = self.client().post('/api/v1/todos/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.todos))
    self.assertEqual(res.status_code, 201)
    json_data = json.loads(res.data)    
    res = self.client().put('/api/v1/todos/' + json_data.get('id'), headers={'Content-Type': 'application/json'}, data=json.dumps(todo1))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(json_data.get('title'), 'Update my test case')

  def test_delete_todo(self):
    """ Test Todo Delete """
    res = self.client().post('/api/v1/todos/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.todos))
    self.assertEqual(res.status_code, 201)
    json_data = json.loads(res.data)
    res = self.client().delete('/api/v1/todos/' + json_data.get('id') , headers={'Content-Type': 'application/json'})
    self.assertEqual(res.status_code, 204)
    
  def tearDown(self):
    """
    Tear Down
    """
    with self.app.app_context():
      db.session.remove()
      db.drop_all()

if __name__ == "__main__":
  unittest.main() 