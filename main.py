from flask import Flask 
from config import DevConfig 
from flask import flask_sqlalchemy import SQLAlchemyfrom config import DevConfigapp = Flask(__name__)app.config.from_object(DevConfig)db = SQLAlchemy(app) 
 
app = Flask(__name__) 
app.config.from_object(DevConfig) 
 
@app.route('/') 
def home(): 
    return '<h1>Hello World!</h1>' 
 
if __name__ == '__main__': 
    app.run() 