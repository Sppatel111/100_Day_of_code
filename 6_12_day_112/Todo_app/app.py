from flask import Flask,render_template,redirect,url_for,request
from sqlalchemy import String, Integer, Date, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import current_user,UserMixin,login_required,logout_user,LoginManager,login_user
from wtforms import StringField,EmailField,DateField,PasswordField, TextAreaField,SelectField,SubmitField
from wtforms.validators import InputRequired,Email,Length
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config['SECRET_KEY'] ='ETRRY5TY767ygrt'
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///todo_app.db"

db.init_app(app)

login_manager=LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#models

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    email: Mapped[str] = mapped_column(primary_key=True, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def get_id(self):
        return self.email


class Task(db.Model):
    __tablename__ = 'tasks'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    is_completed: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[Date] = mapped_column(DateTime, default=datetime.now())
    due_date: Mapped[Date] = mapped_column(DateTime, default=datetime.now())
    priority: Mapped[str] = mapped_column(String, nullable=False)
    user: Mapped[str] = mapped_column(ForeignKey('users.email', ondelete="CASCADE"),nullable=True)

    def __repr__(self):
        return f'<Task {self.id}>'

#forms
class UserLogin(FlaskForm):
    email=EmailField('Email',validators=[InputRequired(),Email()])
    password=PasswordField('Password',validators=[InputRequired()])
    login = SubmitField('Login')

class SignupForm(FlaskForm):
    username=StringField('User Name',validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    Signup=SubmitField('signup')



class CreateTask(FlaskForm):
    title=StringField('Title')
    description=TextAreaField('Description', validators=[InputRequired(), Length(max=300)])
    status=SelectField('Status',
        choices=[('todo', 'TODO'), ('active', 'Active'), ('completed', 'Completed')])
    due_date=DateField('Due Date')
    priority=SelectField('Priority',choices=[('high', 'High'), ('low', 'Low'), ('medium', 'Medium')],default='low')

class UpdateTask(FlaskForm):
    title = StringField('Title')
    description = TextAreaField('Description', validators=[InputRequired(), Length(max=300)])
    status = SelectField('Status',
                         choices=[('todo', 'TODO'), ('active', 'Active'), ('completed', 'Completed')])
    due_date = DateField('Due Date')
    priority = SelectField('Priority', choices=[('high', 'High'), ('low', 'Low'), ('medium', 'Medium')], default='low')


@app.route('/signup',methods=['GET','POST'])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        user1=User(
        email=form.email.data,
        username=form.username.data,
        password=generate_password_hash(form.password.data))
        db.session.add(user1)
        db.session.commit()
        print("signup")
        return redirect(url_for('login'))
    print('not validate')
    return render_template('signup.html',form=form)

@app.route('/',methods=['GET','POST'])
def login():
    form=UserLogin()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user1 = User.query.filter_by(email=email).first()
        if user1 and check_password_hash(user1.password,password):
            print('login success')
            login_user(user1)
            return redirect(url_for('show_tasks'))
        print('invalid')
    print('not validate')
    return render_template('login.html',form=form)

@login_required
@app.route('/logout',methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))


#
@login_required
@app.route('/show',methods=['GET','POST'])
def show_tasks():
    statusf = request.args.get('status', default='all', type=str)

    query = Task.query.filter_by(user=current_user.email)

    if statusf == 'active':
        query = query.filter(Task.is_completed == 'active')
    elif statusf == 'completed':
        query = query.filter(Task.is_completed == 'completed')
    elif statusf == 'todo':
        query = query.filter(Task.is_completed == 'todo')

    task1 = query.all()
    return render_template('tasks.html',task1=task1,statusf=statusf)

@login_required
@app.route('/create', methods=['GET','POST'])
def create_task():
    form=CreateTask()
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
        return redirect(url_for('show_tasks'))
    print('not validate')
    return render_template('create_task.html',form=form)


@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    task2 = Task.query.filter_by(id=task_id).first()
    if task2 is None:
        return "Task not found"
    form = UpdateTask(obj=task2)

    if form.validate_on_submit():
        task2.title = form.title.data
        task2.description = form.description.data
        task2.is_completed = form.status.data
        task2.due_date = form.due_date.data
        task2.priority = form.priority.data
        db.session.commit()
        print('Update successfully!')
        return redirect(url_for('show_tasks'))

    print('Form not validated')
    return render_template('update_task.html', form=form, task2=task2)

@app.route('/delete/<int:id>',methods=['GET','POST'])
def delete_task(id):
    task1 = Task.query.filter_by(id=id).first()
    if request.method == 'GET':
        db.session.delete(task1)
        db.session.commit()
    print('not request method')
    return redirect(url_for('show_tasks'))


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
