from flask import Flask, jsonify, request
from app.router.todo_router import todo_bp

app = Flask(__name__) 

app.register_blueprint(todo_bp)

@app.route('/')
def helloWorld():
     return '<h1>Hello, World!</h1>'
   

if __name__ == '__main__':
  app.run(debug=True)