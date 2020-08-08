import os
from flask import Flask
from config import Config

from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Flask Global Extensions
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()


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
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'login_bp.login'

    # Blueprint imports
    from application.main.main import main_bp
    from application.login.login import login_bp

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(login_bp)

    return app
