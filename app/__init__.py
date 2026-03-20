from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.router.todo_router import todo_bp
    from app.router.operative_route import operative_bp
    app.register_blueprint(todo_bp)
    app.register_blueprint(operative_bp)
    
    @app.route('/')
    def helloWorld():
        return '<h1>Hello, World!</h1>'
    
    return app