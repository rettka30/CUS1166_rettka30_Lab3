import sys
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import *

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/')
def index():
    # Equivalent to: "SELECT * from flights" SQL statement.
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    # Get information from the form.
    if request.method == 'POST':
        course_title = request.form.get('course_title')
        course_number = request.form.get('course_number')
        course = Course(course_title=course_title, course_number=course_number)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_course.html')

@app.route('/register_student/<int:course_id>', methods=['GET', 'POST'])
def register(course_id):
    #
    # Equivalent to "SELECT * from flights where id=flight_id"
    course = Course.query.get(course_id)
    # If this is a post request = Add the passenger.
    if request.method == 'POST':
        name = request.form.get("name")
        grade = request.form.get("grade")
        # Use the utility method to add a new passenger in the database.
        course.add_student(name,grade)
        return redirect(url_for('course'))
    # Use the relationships field in the flights model to retrieve
    # all passengers in the current flight.
    return render_template("register_student.html")

@app.route('/course/<int:course_id>')
def course(course_id):
    course = Course.query.get(course_id)
    students = course.student.order_by().all()
    return render_template("course_details.html", course=course, students=students)

def main():
    if (len(sys.argv)==2):
        print(sys.argv)
    if sys.argv[1] == 'createdb':
        db.create_all()
    else:
        print("Run app using 'flask run")
        print("To create a database use 'python app.py createdb")

if __name__ == "__main__":
    with app.app_context():
        main()
