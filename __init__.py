import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask
from maps.config.config import get_settings
from maps.config.database import db


def create_app():

    settings = get_settings()

    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = settings.JWT_SECRET_KEY  # JWT 토큰을 위한 시크릿 키 설정


    # # Load configurations from settings\
    app.config['SQLALCHEMY_DATABASE_URI'] = '{}://{}:{}@{}:{}/{}'.format(
        settings.DB_TYPE,
        settings.DB_USER,
        settings.DB_PASSWD,
        settings.DB_HOST,
        settings.DB_PORT,
        settings.DB_NAME
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True

    # Initialize extensions
    db.init_app(app)
    
    
    # Register blueprints
    from maps.main import maps_blueprint
    app.register_blueprint(maps_blueprint, url_prefix='/maps')

    return app
