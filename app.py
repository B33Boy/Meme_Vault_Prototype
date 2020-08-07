import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from config import Config

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True, template_folder='application/templates')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_object(Config)

    else:
        app.config.from_mapping(test_config)

    # Flask extensions
    Bootstrap(app)


    # Blueprint imports
    from application.general.general import general_bp
    from application.login.login import login_bp

    # Register blueprints
    app.register_blueprint(general_bp)
    app.register_blueprint(login_bp)

    return app
