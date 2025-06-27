'''
🚩 Problem Statement
Build a simple Student Management System using Python. The system should manage a list of students with their details and provide the following functionalities:
📌 Requirements
Create a class called Student with the following attributes:
name (string)
roll_number (integer)
marks (dictionary with subject names as keys and marks as values)
Add the following methods to the Student class:
get_average_marks(self) – returns the average of all subject marks.
has_passed(self) – returns True if the student has scored at least 40 marks in each subject, otherwise False.
Create another class StudentManager with the following functionalities:
A method add_student(self, student) to add a Student object to the student list.
A method display_all_students(self) to display each student's name, roll number, average marks, and pass/fail status.
A method find_topper(self) that returns the student with the highest average marks.
Demonstrate the working of your classes by:
Creating at least 3 student objects.
Adding them to the StudentManager.
Displaying all student details.
Displaying the topper's name and average marks.

'''

from flask import Flask, render_template, redirect, url_for
from sqlalchemy import String, Integer, JSON, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'htyhrtyerter3435edf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students_data.db'


class Base(DeclarativeBase):
    pass


db = SQLAlchemy()
db.init_app(app)


# models
class Student(db.Model):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    roll_number: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    marks: Mapped[dict] = mapped_column(JSON, nullable=False)
    average: Mapped[int] = mapped_column(Integer, nullable=True)
    has_pass: Mapped[bool] = mapped_column(Boolean, nullable=True)

    def get_average_marks(self, marks):
        print(marks)
        avg = marks['Maths'] + marks['Chemistry'] + marks['Physic'] + marks['English']
        avg /= 4
        return avg

    def has_passed(self, marks):
        print(marks)
        for k, v in marks.items():
            print(v)
            if v < 40:
                return False
        return True


class StudentManager(Student, db.Model):
    def add_student(self, student):
        db.session.add(student)
        db.session.commit()
        print('added succesfully!!')

    def display_all_students(self):
        return Student.query.all()

    def find_topper(self):
        all=Student.query.all()
        dict1={}
        for i in all:
            dict1[i.id]=i.average
        # print(dict1)
        d=sorted(dict1.values(),reverse=True)
        for k,v in dict1.items():
            if v==d[0]:
                return k

# forms
class AddStudent(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    roll_number = StringField('Roll No.', validators=[InputRequired()])
    maths = IntegerField('Maths', validators=[InputRequired()])
    chemistry = IntegerField('Chemistry', validators=[InputRequired()])
    physic = IntegerField('Physic', validators=[InputRequired()])
    english = IntegerField('English', validators=[InputRequired()])
    add = SubmitField('Add')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/show',methods=['GET','POST'])
def show():
    s = StudentManager()
    all=s.display_all_students()
    return render_template('show.html',all=all)

@app.route('/topper',methods=['GET','POST'])
def topper():
    manager=StudentManager()
    student_id=manager.find_topper()
    top=Student.query.filter_by(id=student_id).first()
    return render_template('topper.html',top=top)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddStudent()
    sobject = Student()
    if form.validate_on_submit():
        marks1 = {
            'Maths': form.maths.data,
            'Physic': form.physic.data,
            'Chemistry': form.chemistry.data,
            'English': form.english.data
        }
        s = Student(
            name=form.name.data,
            roll_number=form.roll_number.data,
            marks={
                'Maths': form.maths.data,
                'Physic': form.physic.data,
                'Chemistry': form.chemistry.data,
                'English': form.english.data
            },
            average=sobject.get_average_marks(marks1),
            has_pass=sobject.has_passed(marks1)
        )
        stu = StudentManager()
        stu.add_student(s)
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
