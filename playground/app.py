import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import *

app = Flask(name)
app.config.from_object(Config)

db.init_app(app)

@app.route('/')
def index():
    pass

@app.route('/add_course')
def add_course():
    pass

@app.route('/register_student/', methods=['GET', 'POST'])
def register():
    pass

if __name__ == "__main__":
    with app.app_context():
        main()
