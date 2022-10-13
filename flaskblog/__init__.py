import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '40230906a702d2d89c6621c6d30a9b4f' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
