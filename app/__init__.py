from flask import Flask
from config import Config

def CreateApp():
    config_class=Config
    app=Flask(__name__)
    app.config.from_object(config_class)
    
    from app import routes
    app.register_blueprint(main)
    return app