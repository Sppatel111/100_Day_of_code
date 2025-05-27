# Hotel Room Booking System
# Classes like Room, Customer, Booking, using composition and encapsulation.
from flask import Flask, render_template ,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Date, DateTime,ForeignKey,ForeignKeyConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime
from flask_login import login_user,logout_user,login_required,current_user,UserMixin,LoginManager
from wtforms import StringField,SubmitField,EmailField,SelectField,PasswordField, IntegerField,DateField
from wtforms.validators import Length,Email,InputRequired
from flask_wtf import FlaskForm


app = Flask(__name__)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app.config['SECRET_KEY'] = 'RWQERQWEQWE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel_management.db'
db.init_app(app)
login_manager=LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Customer.query.get(user_id)
# models
class Customer(UserMixin,db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    phone: Mapped[str] = mapped_column(String, nullable=False)
    password:Mapped[str]=mapped_column(String,nullable=False)
    created_at: Mapped[Date] = mapped_column(DateTime, default=datetime.now())

    def __repr__(self):
        return f'<Customer {self.id}>'


class Room(db.Model):
    __tablename__ = 'rooms'
    id: Mapped[int] = mapped_column(Integer,autoincrement=True, primary_key=True)
    type: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    price:Mapped[int]=mapped_column(Integer,nullable=False)

    booking = relationship('Booking', back_populates='rooms')

    def __repr__(self):
        return f'<Room {self.id}>'


class Booking(db.Model):
    __tablename__ = 'booking'
    id: Mapped[int] = mapped_column(Integer,autoincrement=True ,primary_key=True)
    customer_id:Mapped[int]=mapped_column(ForeignKey('users.id',ondelete="CASCADE"))
    booked_date: Mapped[Date] = mapped_column(DateTime,default=datetime.now())
    leave_date:Mapped[Date]=mapped_column(DateTime,nullable=True)
    room_id: Mapped[int] = mapped_column(Integer,nullable=False)
    __table_args__ = (ForeignKeyConstraint
                      (['room_id'], ['rooms.id'], ondelete='CASCADE'),
                      )

    rooms = relationship('Room', back_populates='booking')

    def __repr__(self):
        return f'<Booking {self.id}>'


#forms

class SignupForm(FlaskForm):
    name=StringField('Name',validators=[InputRequired()])
    email=StringField('Email',validators=[InputRequired(),Email()])
    password=PasswordField('Password',validators=[InputRequired()])
    phone=StringField('Phone',validators=[InputRequired()])
    signup=SubmitField('Signup')

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[InputRequired(),Email()])
    password=PasswordField('Password',validators=[InputRequired()])
    login=SubmitField('Login')

class AddRoomForm(FlaskForm):
    type=SelectField('Type',choices=[('small','Small'),('medium','Medium'),('hi-fi','Hi-Fi')])
    status=SelectField('Status',choices=[('available','Available'),('not-available','Not-Available')])
    price=IntegerField('Price',validators=[InputRequired()])
    add=SubmitField('Add')

class BookedForm(FlaskForm):
    booked_date=DateField('Booked Date')
    leave_date=DateField('Leave Date')
    Booking_room=SubmitField('Booking_Room')

@app.route('/signup',methods=['GET','POST'])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        u=Customer(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data,
            phone=form.phone.data

        )
        db.session.add(u)
        db.session.commit()
        print('signin')
        return redirect(url_for('login'))
    print('not validate')
    return render_template('signup.html',form=form)


@app.route('/',methods=['GET','POST'])
def login():
    form=LoginForm()
    email = form.email.data
    password = form.password.data
    user1=Customer.query.filter_by(email=email).first()
    if form.validate_on_submit():
        if email and password == user1.password:
            login_user(user1)
            print(current_user)
            return redirect(url_for('home'))
    return render_template('login.html',form=form)

@app.route('/logout',methods=['POST','GET'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_required
@app.route('/home', methods=['GET','POST'])
def home():
    room1=Room.query.all()
    return render_template('home.html',room1=room1)

@login_required
@app.route('/history', methods=['GET','POST'])
def booked_detail():
    detail=Booking.query.filter_by(id=current_user.id).all()
    return render_template('booked_detail.html',detail=detail)


from datetime import datetime
@login_required
@app.route('/booking/<int:id>',methods=['GET','POST'])
def room_booking(id):
    room1=Room.query.filter_by(id=id).first()
    form=BookedForm()
    if form.validate_on_submit():
        print('yes')
        booking=Booking(
            customer_id=current_user.id,
            booked_date=form.booked_date.data,
            leave_date=form.leave_date.data,
            room_id=id
        )
        # if form.leave_date.data > datetime.now():
        room1.status='not-available'
        db.session.add(booking)
        db.session.commit()
        print('booked')
        return redirect(url_for('home'))
    print('not validate')
    return render_template('booking.html',r=room1,form=form)

#admin

@app.route('/add',methods=['GET','POST'])
def add_rooms():
    form=AddRoomForm()
    if form.validate_on_submit():
        room1=Room(
            type=form.type.data,
            status=form.status.data,
            price=form.price.data
        )
        db.session.add(room1)
        db.session.commit()
        print('add room')
        return redirect(url_for('home'))
    print('not validate')
    return render_template('add_rooms.html',form=form)

@app.route('/all' ,methods=['GET','POST'])
def all_rooms():
    form=AddRoomForm()
    room1=Room.query.all()
    return render_template('admin_all_rooms.html',form=form,room1=room1)

@app.route('/update/<int:id>',methods=['GET','POST'])
def update_room_status(id):
    room1=Room.query.filter_by(id=id).first()
    if room1.status == 'not-available':
        room1.status ='available'
        print('yes')
    else:
        room1.status ='not-available'
        print('no')
    db.session.commit()
    return redirect(url_for('all_rooms'))

@app.route('/show/<int:id>',methods=['GET','POST'])
def show_booking(id):
    booked=Booking.query.filter_by(room_id=id).all()
    return render_template('show_booking.html',booked=booked)
    

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
