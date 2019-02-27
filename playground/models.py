from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Course(db.Model):
    __tablename__= "course"
    id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.String(32), index=True)
    course_title = db.Column(db.String(64), index=True)
    student = db.relationship('RegisteredStudent', backref='course', lazy=True)

    def add_student(self,name,grade):
        # Notice that we set the foreign key for the passenger class.
        new_student = RegisteredStudent(name=name, grade=grade, course_id=self.id )
        db.session.add(new_student)
        db.session.commit()


class RegisteredStudent(db.Model):
    __tablename__= "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=False)
    grade = db.Column(db.Float)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
