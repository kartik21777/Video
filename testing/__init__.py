from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = '\x89\xc8\xf1\xc2&\x87\xf6\xa1\x13C\xd5\x89'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:21122004@localhost/vis'
db = SQLAlchemy(app)
migrate = Migrate(app,db)
from testing import route