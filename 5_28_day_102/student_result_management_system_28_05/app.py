# Student Result Management System

# Define Student class with methods to add grades, calculate average, and generate report cards.


from flask import Flask, redirect, render_template, url_for
from sqlalchemy import String, Integer, ForeignKey,and_
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from wtforms import IntegerField, SubmitField, SelectField, StringField, TextAreaField
from wtforms.validators import InputRequired, Length
from flask_wtf import FlaskForm
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'FEDRTFEDRTWERSDF'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

db.init_app(app)
migrate = Migrate(app, db)




# models
class Student(db.Model):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    enroll_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String, nullable=False)


    subjects = relationship('Subject', back_populates='students')

    def __repr__(self):
        return f'<Student {self.id}>'

    def grades(self, id, sub, marks, sem):
        sub1 = Subject(
            subject=sub,
            score=marks,
            semester=sem,
            student_id=id
        )
        db.session.add(sub1)
        db.session.commit()

    def avg(self, s_id, sem):

        grade = Subject.query.filter(and_(Subject.student_id == s_id, Subject.semester == sem)).all()
        list1 = 0
        for i in grade:
            list1 += i.score
        print(list1)

        return list1


class Subject(db.Model):
    __tablename__ = 'subjects'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subject: Mapped[str] = mapped_column(String, nullable=False)
    score: Mapped[int] = mapped_column(Integer, nullable=False)
    semester: Mapped[str] = mapped_column(String, nullable=False)
    student_id: Mapped[str] = mapped_column(ForeignKey('students.id', ondelete='CASCADE'))

    students = relationship('Student', back_populates='subjects')


# froms
class StudentForm(FlaskForm):
    enroll_id = StringField('Enroll_No', validators=[InputRequired()])
    full_name = StringField('Full Name', validators=[InputRequired()])
    Enroll = SubmitField('Enroll')


class SubjectForm(FlaskForm):
    subject = StringField('Subject', validators=[InputRequired()])
    score = IntegerField('Score', validators=[InputRequired()])
    semester = SelectField('Semester', choices=[('sem1', 'SEM1'), ('sem2', 'SEM2'), ('sem3', 'SEM3'), ('sem4', 'SEM4')])
    add = SubmitField('ADD')


@app.route('/', methods=['GET', 'POST'])
def home():
    student = Student.query.all()
    return render_template('home.html', student=student)


@app.route('/add', methods=['GET', 'POST'])
def add_students():
    form = StudentForm()
    if form.validate_on_submit():
        s = Student(
            enroll_id=form.enroll_id.data,
            full_name=form.full_name.data
        )
        db.session.add(s)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add_students.html', form=form)


@app.route('/view/<int:id>', methods=['GET', 'POST'])
def view_student(id):
    s1 = Student.query.filter_by(id=id).first()
    sub1 = Subject.query.filter_by(student_id=id).all()
    return render_template('view_student.html', s1=s1, sub1=sub1)


@app.route('/add-subject/<int:id>', methods=['GET', 'POST'])
def add_subject(id):
    form = SubjectForm()
    if form.validate_on_submit():
        sub1 = form.subject.data
        score = form.score.data
        semester = form.semester.data
        s = Student()
        s.grades(id, sub1, score, semester)
        print('done')
        return redirect(url_for('view_student', id=id))
    print('not validate')
    return render_template('add_subject.html', form=form)


@app.route('/card/<int:id>', methods=['GET', 'POST'])
def score_card(id):
    s1 = Student.query.filter_by(id=id).first()
    sub1 = Subject.query.filter_by(student_id=id).order_by(Subject.semester).all()
    s = Student()

    s.avg(id,'sem1')
    return render_template('score_card.html', s1=s1, sub1=sub1,s=s)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
