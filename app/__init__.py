from flask import Flask
from config import Config
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'

def CreateApp(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.routes import main
    app.register_blueprint(main)

    login_manager.init_app(app)

    return app
