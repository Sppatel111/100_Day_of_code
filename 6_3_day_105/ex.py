# Class Employee with inheritance to Manager, Developer, etc., and methods for payroll.

from flask import Flask, redirect, render_template, url_for
from sqlalchemy import String, Integer, DateTime, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import InputRequired
from flask_login import LoginManager, UserMixin, login_required, logout_user, login_user
from datetime import datetime
from flask_wtf import FlaskForm

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app.config['SECRET_KEY'] = 'ERWERQWERRsfsef'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(user_id)


# models

class Employee(Base, UserMixin, db.Model):
    __tablename__ = 'employee'
    email: Mapped[str] = mapped_column(String, primary_key=True, unique=True)
    emp_name: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    salary: Mapped[int] = mapped_column(Integer, default=0)
    hire_date: Mapped[Date] = mapped_column(DateTime, default=datetime.now())

    def __repr__(self):
        return f'<Employee {self.email}>'

    def get_id(self):
        return self.email

    def __init__(self, emp_name, email, password, salary=5000, hire_date=datetime.now()):
        self.emp_name = emp_name
        self.email = email
        self.password=password
        self.salary = salary
        self.hire_date = hire_date

    def calculate_payroll(self):
        return self.salary


class Manager(Employee, db.Model):
    __tablename__ = 'manager'
    e_id: Mapped[int] = mapped_column(ForeignKey("employee.email"), primary_key=True)
    # d_id:Mapped[int]=mapped_column(Integer,primary_key=True,unique=True)
    department: Mapped[str] = mapped_column(String, nullable=False)

    def __init__(self, name, employee_id, salary, hire_date, department):
        super().__init__(name, employee_id, salary, hire_date)
        self.department = department

    def calculate_payroll(self):
        bonus = self.salary * 0.1
        return self.salary + bonus


class Developer(Employee, db.Model):
    __tablename__ = 'developer'
    e_id: Mapped[int] = mapped_column(ForeignKey("employee.email"), primary_key=True)
    programming_lang: Mapped[str] = mapped_column(String)

    def __init__(self, name, employee_id, salary, hire_date, programming_lang):
        super().__init__(name, employee_id, salary, hire_date)
        self.programming_lang = programming_lang

    def calculate_payroll(self):
        project_bonus = self.salary * 0.05
        return self.salary + project_bonus


# forms
class SignupForm(FlaskForm):
    emp_name = StringField('Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    signup = SubmitField('Signup')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    login = SubmitField('Login')


# urls
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        e1 = Employee(
            emp_name=form.emp_name.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(e1)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    email = form.email.data
    password = form.password.data
    e1 = Employee.query.filter_by(email=email).first()
    if form.validate_on_submit():
        if e1 and e1.password == password:
            login_user(e1)
            return redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
