# Flight Reservation System
#
# Use classes for Flight, Passenger, Booking, using inheritance and file handling.

from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from wtforms import StringField, IntegerField, SubmitField, EmailField, PasswordField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ERFERwerwerwer'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flights.db'


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Passengers.query.get(user_id)


# models
class Person(db.Model):
    __abstract__ = True
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f'<Person {self.id}>'


class Passengers(Person, UserMixin):
    __tablename__ = 'passengers'
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)


    booking = relationship('Booking', back_populates='passengers')


class Flight(db.Model):
    __tablename__ = 'flights'
    id: Mapped[str] = mapped_column(Integer, primary_key=True, autoincrement=True)
    flight_number: Mapped[str] = mapped_column(String, nullable=False)
    origin: Mapped[str] = mapped_column(String, nullable=False)
    destination: Mapped[str] = mapped_column(String, nullable=False)
    seats: Mapped[int] = mapped_column(Integer, nullable=False)

    booking = relationship('Booking', back_populates='flights')


class Booking(db.Model):
    __tablename__ = 'booking'
    id: Mapped[str] = mapped_column(Integer, primary_key=True, autoincrement=True)
    fight_id: Mapped[int] = mapped_column(Integer, ForeignKey('flights.id', ondelete='CASCADE'))
    passenger_id: Mapped[int] = mapped_column(Integer, ForeignKey('passengers.id', ondelete='CASCADE'))

    passengers = relationship('Passengers', back_populates='booking')
    flights = relationship('Flight', back_populates='booking')


# forms
class SignupForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    signup = SubmitField('Signup')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    login = SubmitField('Login')


class AddFlight(FlaskForm):
    flight_number = StringField('Flight Number', validators=[InputRequired()])
    origin = StringField('Origin', validators=[InputRequired()])
    destination = StringField('Destination', validators=[InputRequired()])
    seats = IntegerField('Seats', validators=[InputRequired()])
    add = SubmitField('Add')


class BookingForm(FlaskForm):
    book_now = SubmitField('Book Now')


# urls
@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    email = form.email.data
    password = form.password.data
    user1 = Passengers.query.filter_by(email=email).first()
    if form.validate_on_submit():
        if user1 and user1.password == password:
            login_user(user1)
            return redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user1 = Passengers(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user1)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@login_required
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('logout'))

@login_required
@app.route('/home', methods=['GET', 'POST'])
def home():
    f1 = Flight.query.all()
    return render_template('home.html', f1=f1)

@login_required
@app.route('/booking/<int:id>', methods=['GET', 'POST'])
def booking(id):
    flag = False
    f1 = Booking.query.filter_by(passenger_id=current_user.id).all()
    f = Flight.query.filter_by(id=id).first()
    for x in f1:
        if x.fight_id == f.id:
            flag = True

    form = BookingForm()
    if form.validate_on_submit():
        if flag == False:
            booked = Booking(
                fight_id=id,
                passenger_id=current_user.id
            )
            f.seats = f.seats-1
            db.session.add(booked)
            db.session.commit()
            log_booking(f.flight_number,current_user.name)
            return redirect(url_for('home'))

    return render_template('booking.html', f=f, form=form,flag=flag)


@login_required
@app.route('/history', methods=['GET', 'POST'])
def history():
    f1 = Booking.query.filter_by(passenger_id=current_user.id).all()
    return render_template('history.html', f1=f1)


# admin urls
@app.route('/add', methods=['GET', 'POST'])
def add_flights():
    form = AddFlight()
    if form.validate_on_submit():
        f1 = Flight(
            flight_number=form.flight_number.data,
            origin=form.origin.data,
            destination=form.destination.data,
            seats=form.seats.data
        )
        db.session.add(f1)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_flights.html', form=form)

def log_booking(flight_number,passenger):
    with open(f'{flight_number}_{passenger}.txt','w') as f:
        f.write(f'Dear {passenger}, Your flight ticket are booked {flight_number}.')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
