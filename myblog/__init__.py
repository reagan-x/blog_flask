from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Cargar las configuraciones
app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:k2grVzkGfPnf_Ei@localhost:3306/blog_db"
db = SQLAlchemy(app)

#Importar vistas 
from myblog.views.auth import auth
app.register_blueprint(auth)

from myblog.views.blog import blog
app.register_blueprint(blog)
app.add_url_rule('/', endpoint='index')

with app.app_context():
    db.create_all()
