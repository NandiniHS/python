from flask import Flask
from flask_jwt_extended import JWTManager
from database import init_app
from routes.auth import auth_bp
from routes.protected import protected_bp

app = Flask(__name__)


app.config['JWT_SECRET_KEY'] = 'b10b867a86e2127f2c88edd70a251147687758af378ddb02c0bba83cb8ebe893'



init_app(app)
jwt = JWTManager(app)





app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(protected_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
