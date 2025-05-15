from flask import Flask,render_template,redirect,url_for, request
from sqlalchemy import String,DateTime,ForeignKey,Integer,create_engine
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from flask_sqlalchemy import SQLAlchemy
from wtforms import PasswordField,EmailField,StringField,DateField,SubmitField,SelectField, TextAreaField
from wtforms.validators import InputRequired,Email, DataRequired ,Length
from flask_wtf import FlaskForm
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager ,current_user ,UserMixin,login_required,login_user,logout_user

user='postgres'
password='1234567'
host='localhost'
port='5432'
database='todo1'

class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)

app=Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'
#app.config['SQLALCHEMY_DATABASE_URI'] =f'postgresql://{user}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql://postgres:1234567@localhost:5432/todo"

db.init_app(app)

migrate=Migrate()
migrate.init_app(app,db)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # return User.get(user_id)
    return User.query.get(user_id)


# connection_str= f'postgresql://{user}:{password}@{host}:{port}/{database}'
# engine=create_engine(connection_str)
#
# try:
#     with engine.connect() as connection_str:
#         print("succesfully connected")
# except Exception as e:
#     print(e)

#models

class User(UserMixin,db.Model):
    __tablename__='users'
    # id:Mapped[int]=mapped_column(Integer,primary_key=True, autoincrement=True)
    # email:Mapped[str]=mapped_column(String,unique=True,nullable=False)
    email: Mapped[str] = mapped_column(primary_key=True, unique=True, nullable=False)
    username:Mapped[str]=mapped_column(String,nullable=False)
    password:Mapped[str]=mapped_column(String,nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'
    # id to email
    def get_id(self):
        return self.email

class Task(db.Model):
    __tablename__='tasks'
    id:Mapped[int]=mapped_column(Integer, primary_key=True, autoincrement=True)
    title:Mapped[str]=mapped_column(String,nullable=False)
    description: Mapped[str] = mapped_column(String,nullable=False)
    is_completed: Mapped[str] = mapped_column(String,nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime,default=datetime.now())
    due_date: Mapped[datetime] = mapped_column(DateTime,nullable=False)
    priority: Mapped[str] = mapped_column(String,nullable=False)
    user: Mapped[str] = mapped_column(ForeignKey('users.email', ondelete="CASCADE"),nullable=False)

    def __repr__(self):
        return f'<Task {self.id}>'


#forms.py
class LoginForm(FlaskForm):
    email=EmailField('Email',validators=[Email(),InputRequired()])
    password=PasswordField('Password',validators=[InputRequired()])
    login = SubmitField('Login')

class SignupForm(FlaskForm):
    username=StringField('User Name',validators=[InputRequired()])
    email = EmailField('Email', validators=[Email(), InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    Signup = SubmitField('signup')

class CreateTaskForm(FlaskForm):
    title=StringField('Title')
    description=TextAreaField('Description', validators=[DataRequired(), Length(max=300)])
    status=SelectField('Status',
        choices=[('todo', 'TODO'), ('active', 'Active'), ('completed', 'Completed')])
    due_date=DateField('Due Date')
    priority=SelectField('Priority',choices=[('high', 'High'), ('low', 'Low'), ('medium', 'Medium')],default='low')

class UpdateTaskForm(FlaskForm):
    title = StringField('Title')
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=300)])
    status = SelectField('Status',
                         choices=[('todo', 'TODO'), ('active', 'Active'), ('completed', 'Completed')])
    due_date = DateField('Due Date')
    priority = SelectField('Priority', choices=[('high', 'High'), ('low', 'Low'), ('medium', 'Medium')], default='low')

#templetes
@app.route('/signup',methods=['GET','POST'])
def signup():
    form= SignupForm()
    if form.validate_on_submit():
        print('submit')

        user=User(username=form.username.data,
        email=form.email.data,
        password = generate_password_hash(form.password.data))
        #password = generate_password_hash(form.password.data)
        db.session.add(user)
        db.session.commit()
        print('add user succesfully')
        return redirect(url_for('login'))

    print('not validate or not added')
    return render_template('register.html',form=form)

@app.route('/',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user1 = User.query.filter_by(email=email).first()
        if user1 and check_password_hash(user1.password,password):
            print('login success')
            login_user(user1)
            return redirect(url_for('show'))
        print('invalid')
    print('not validate')
    return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_required
@app.route('/show-task',methods=['GET','POST'])
def show():
    status_filter = request.args.get('status', default='all', type=str)

    query = Task.query.filter_by(user=current_user.email)

    if status_filter == 'active':
        query = query.filter(Task.is_completed == 'active')
    elif status_filter == 'completed':
        query = query.filter(Task.is_completed == 'completed')
    elif status_filter == 'todo':
        query = query.filter(Task.is_completed == 'todo')

    task1 = query.all()
    return render_template('tasks.html',task1=task1,status_filter=status_filter)

@login_required
@app.route('/create', methods=['GET','POST'])
def create_task():
    form=CreateTaskForm()
    if form.validate_on_submit():
        print(current_user)
        task1=Task(
            title=form.title.data,
            description = form.description.data,
            is_completed = form.status.data,
            due_date = form.due_date.data,
            priority = form.priority.data,
            user=current_user.email
        )
        db.session.add(task1)
        db.session.commit()
        print('added successfully!')
        return redirect(url_for('show'))
    print('not validate')
    return render_template('create_task.html',form=form)


@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    task2 = Task.query.filter_by(id=task_id).first()
    if task2 is None:
        return "Task not found"
    form = UpdateTaskForm(obj=task2)

    if form.validate_on_submit():
        task2.title = form.title.data
        task2.description = form.description.data
        task2.is_completed = form.status.data
        task2.due_date = form.due_date.data
        task2.priority = form.priority.data
        db.session.commit()
        print('Update successfully!')
        return redirect(url_for('show'))

    print('Form not validated')
    return render_template('update_task.html', form=form, task2=task2)

@app.route('/delete/<int:id>',methods=['GET','POST'])
def delete_task(id):
    task1 = Task.query.filter_by(id=id).first()
    if request.method == 'GET':
        db.session.delete(task1)
        db.session.commit()
    print('not request method')
    return redirect(url_for('show'))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)


