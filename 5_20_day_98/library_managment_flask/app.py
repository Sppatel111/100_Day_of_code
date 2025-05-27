from flask import Flask, redirect, url_for, render_template
from sqlalchemy import String, Integer, ForeignKeyConstraint, Date, DateTime, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from wtforms import StringField, SubmitField, EmailField, PasswordField, IntegerField, TextAreaField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import email, InputRequired, Length
from datetime import datetime

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app.config['SECRET_KEY'] = 'ERERERertrtertwe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Member.query.get(user_id)


# models
class Member(UserMixin, db.Model):
    __tablename__ = 'members'
    email: Mapped[str] = mapped_column(String, primary_key=True, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False)
    phone: Mapped[int] = mapped_column(Integer, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)


    def __repr__(self):
        return f'<Member {self.email}>'

    def get_id(self):
        return self.email


class Book(db.Model):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    added: Mapped[Date] = mapped_column(DateTime, default=datetime.now())


class Library(db.Model):
    __tablename__ = 'libraries'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    # book_name:Mapped[str]=mapped_column(String,nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    taken_date: Mapped[Date] = mapped_column(DateTime, default=datetime.now())
    return_date: Mapped[Date] = mapped_column(DateTime, nullable=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id', ondelete="CASCADE"), nullable=True)




# forms
class SignupForm(FlaskForm):
    username = StringField('User Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[email(), InputRequired()])
    phone = StringField('Phone', validators=[InputRequired()])
    address = TextAreaField('Address', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6)])
    register = SubmitField('Register')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[email(), InputRequired()])
    password = PasswordField('Email', validators=[InputRequired(), Length(min=6)])
    login = SubmitField('Login')


class AddBook(FlaskForm):
    name = StringField('Book Name', validators=[InputRequired()])
    status = SelectField('Status', choices=[('available', 'Available'), ('not_available', 'Not_Available')])
    add = SubmitField('Add')


class UpdateBook(FlaskForm):
    name = StringField('Book Name', validators=[InputRequired()])
    status = SelectField('Status', choices=[('available', 'Available'), ('not_available', 'Not_Available')])
    update = SubmitField('Update')

class ReturnBook(FlaskForm):
    return_book=SubmitField('Return')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user1 = Member(
            email=form.email.data,
            username=form.username.data,
            phone=form.phone.data,
            address=form.address.data,
            password=form.password.data

        )
        db.session.add(user1)
        db.session.commit()
        print('signup')
        return redirect(url_for('login'))
    print('not signup validate')
    return render_template('signup.html', form=form)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user1 = Member.query.filter_by(email=email).first()
        print(user1)
        if user1 and user1.password == password:
            print(current_user)
            print(email)
            print(password)
            login_user(user1)
            print('login')
            return redirect(url_for('home'))
        print('not login')
    print('not login validate')

    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home', methods=['GET', 'POST'])
def home():
    all_books = Book.query.all()
    return render_template('home.html', all_books=all_books)


@app.route('/borrow/<int:id>', methods=['GET', 'POST'])
def borrow(id):
    b1 = Book.query.filter_by(id=id).first()
    return render_template('borrow.html', b1=b1)


@app.route('/borrow_by_person/<int:id>', methods=['GET', 'POST'])
def borrow_by_person(id):
    b1 = Book.query.filter_by(id=id).first()
    if b1:
        l1 = Library(
            email=current_user.email,
            book_id=b1.id
        )
        db.session.add(l1)
        db.session.commit()
        print('borrow')
        return redirect(url_for('history'))



@app.route('/history', methods=['GET', 'POST'])
def history():
    history = Library.query.filter_by(email=current_user.email).all()
    return render_template('history.html', history=history)


@app.route('/show/<int:id>', methods=['GET', 'POST'])
def show(id):
    detail = Book.query.filter_by(id=id).first()
    return render_template('book_detail.html', detail=detail)

@app.route('/return/<int:id>', methods=['GET', 'POST'])
def return_book(id):
    l1=Library.query.filter_by(id=id).first()
    detail = Book.query.filter_by(id=l1.book_id).first()
    form=ReturnBook()
    if form.validate_on_submit():
        l1.return_date=datetime.now()
        db.session.commit()
        print('return')
        return redirect(url_for('history'))
    print('not validate')
    return render_template('return_book.html',l1=l1,detail=detail,form=form)

# admin
@app.route('/add', methods=['GET', 'POST'])
def insert():
    form = AddBook()
    if form.validate_on_submit():
        book1 = Book(
            name=form.name.data,
            status=form.status.data
        )
        db.session.add(book1)
        db.session.commit()
        print('insert')
        return redirect(url_for('home'))
    print('not validate')
    return render_template('add_book.html', form=form)


@app.route('/askupdate', methods=['GET', 'POST'])
def ask_update():
    all_books = Book.query.all()
    return render_template('update_book.html', all_books=all_books)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    b1 = Book.query.filter_by(id=id).first()
    form = UpdateBook(obj=b1)
    if form.validate_on_submit():
        b1.name = form.name.data
        b1.status = form.status.data
        db.session.commit()
        print('update')
        return redirect(url_for('ask_update'))
    print('not validate')
    return render_template('update_status.html', form=form, b1=b1)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
