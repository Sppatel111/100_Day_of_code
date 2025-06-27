# Class Employee with inheritance to Manager, Developer, etc., and methods for payroll.

from flask import Flask, redirect, render_template, url_for
from sqlalchemy import String, Integer, DateTime, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, EmailField, PasswordField,SelectField
from wtforms.validators import InputRequired
from flask_login import LoginManager, UserMixin, login_required, logout_user, login_user
from datetime import datetime
from flask_wtf import FlaskForm
from flask_migrate import Migrate

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app.config['SECRET_KEY'] = 'ERWERQWERRsfsef'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
migrate=Migrate()
migrate.init_app(app,db)

@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(user_id)


# models
class Employee(Base, UserMixin, db.Model):
    __tablename__ = 'employee'
    id:Mapped[int]=mapped_column(Integer,autoincrement=True,primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    emp_name: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    salary: Mapped[int] = mapped_column(Integer, default=0)
    hire_date: Mapped[Date] = mapped_column(DateTime, default=datetime.now())
    type: Mapped[str] = mapped_column(String, nullable=False)
    end_date:Mapped[Date]=mapped_column(DateTime,nullable=True)
    status:Mapped[str]=mapped_column(String,nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'employee',
        'polymorphic_on': type,
        'with_polymorphic': '*'
    }

    def __repr__(self):
        return f'<Employee {self.id}>'



    def __init__(self, emp_name, email, password,type,salary=50000, hire_date=datetime.now()):
        self.emp_name = emp_name
        self.email = email
        self.password = password
        self.salary = salary
        self.hire_date = hire_date
        self.type = type

    def calculate_payroll(self):
        return self.salary


class Manager(Employee,):
    __mapper_args__ = {
        'polymorphic_identity': 'manager',
    }

    def calculate_payroll(self):
        bonus = self.salary * 0.1
        return self.salary + bonus


class Developer(Employee):
    __mapper_args__ = {
        'polymorphic_identity': 'developer',
    }

    def calculate_payroll(self):
        project_bonus = self.salary * 0.05
        return self.salary + project_bonus


# forms
class AddEmpForm(FlaskForm):
    emp_name = StringField('Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    type=SelectField('Type',choices=[('manager','manager'),('developer','developer')])
    signup = SubmitField('Signup')


# class LoginForm(FlaskForm):
#     email = EmailField('Email', validators=[InputRequired()])
#     password = PasswordField('Password', validators=[InputRequired()])
#     login = SubmitField('Login')


# urls
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddEmpForm()
    if form.validate_on_submit():
        emp_name = form.emp_name.data,
        email = form.email.data,
        password = form.password.data,
        type = form.type.data

        if type=='manager':
            emp=Manager(emp_name,email,password,type)
        elif type=='developer':
            emp=Developer(emp_name,email,password,type)
        else:
            emp=Employee()
        e1 = Employee(
            emp_name=form.emp_name.data,
            email=form.email.data,
            password=form.password.data,
            type=form.type.data,
            salary=emp.calculate_payroll(),
            status='Present'
        )
        db.session.add(e1)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

# @app.route('/', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     email = form.email.data
#     password = form.password.data
#     e1 = Employee.query.filter_by(email=email).first()
#     if form.validate_on_submit():
#         if e1 and e1.password == password:
#             login_user(e1)
#             return redirect(url_for('home'))
#     return render_template('login.html', form=form)
#
#
# @app.route('/logout', methods=['GET', 'POST'])
# def logout():
#     logout_user()
#     return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
def home():
    emp=Employee.query.all()
    return render_template('home.html',emp=emp)

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    emp1=Employee.query.filter_by(id=id).first()
    if emp1.type=='manager':
        emp = Developer(emp1.emp_name, emp1.email, emp1.password, emp1.type)
        emp1.type='developer'
        emp1.salary=emp.calculate_payroll()
    elif emp1.type =='developer':
        emp = Manager(emp1.emp_name, emp1.email, emp1.password, emp1.type)
        emp1.type='manager'
        emp1.salary = emp.calculate_payroll()
    else:
        emp1.type='employee'
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update-status/<int:id>',methods=['GET','POST'])
def update_status(id):
    a=Employee.query.filter_by(id=id).first()
    if a.status =='Present':
        a.status ='Not-Present'
        a.end_date=datetime.now()
    elif a.status == 'Not-Present':
        a.status='Present'
        a.end_date=None
    else:
        a.status='Present'
    db.session.commit()
    return redirect(url_for('home'))


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
