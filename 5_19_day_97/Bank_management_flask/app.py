from flask import Flask,redirect,url_for,render_template
from sqlalchemy import String,Integer,ForeignKeyConstraint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase,relationship
from flask_login import LoginManager,login_user,logout_user,login_required,current_user,UserMixin
from wtforms import StringField,SubmitField,EmailField, PasswordField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import email,InputRequired,Length
from werkzeug.security import check_password_hash,generate_password_hash
from datetime import datetime
app=Flask(__name__)

class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)

app.config['SECRET_KEY']='ERERERertrtertwe'
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Bank_management_flask/database.db'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
db.init_app(app)
login_manager=LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#models
class User(UserMixin,db.Model):
    __tablename__='users'
    email:Mapped[str]=mapped_column(String,primary_key=True,unique=True,nullable=False)
    username:Mapped[str]=mapped_column(String,nullable=False)
    password:Mapped[str]=mapped_column(String,nullable=False)

    accounts = relationship("Account", back_populates="users",uselist=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def get_id(self):
        return self.email

class Account(db.Model):
    __tablename__='accounts'
    owner: Mapped[str] = mapped_column(String, primary_key=True)
    balance: Mapped[int] = mapped_column(Integer,default=0)

    __table_args__ = (ForeignKeyConstraint
                      (['owner'], ['users.email'], ondelete='CASCADE'),
                      )
    users = relationship("User", back_populates="accounts")

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,d):
        self.balance +=d
        return self.balance

    def withdraw(self,w):
        if w <= self.balance:
            self.balance -= w
            return self.balance
        else:
            print('insufficient')

    def check_balance(self):
        print(f'total balance {self.balance}')
        return self.balance


# forms
class SignupForm(FlaskForm):
    email=EmailField('Email',validators=[email(),InputRequired()])
    username=StringField('User Name', validators=[InputRequired()])
    password = PasswordField('Email', validators=[InputRequired(),Length(min=6)])
    register=SubmitField('Register')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[email(), InputRequired()])
    password = PasswordField('Email', validators=[InputRequired(), Length(min=6)])
    login=SubmitField('Login')

class DepositForm(FlaskForm):
    amount= IntegerField('Amount',validators=[InputRequired()])
    fdeposit = SubmitField('Deposit')

class WithdrawForm(FlaskForm):
    amount = IntegerField('Amount', validators=[InputRequired()])
    fwithdraw = SubmitField('Withdraw')

## classes
@app.route('/signup',methods=['GET','POST'])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        user1=User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data
        )
        account1=Account(
            owner=form.email.data,
            balance=0
        )
        db.session.add(user1)
        db.session.commit()
        db.session.add(account1)
        db.session.commit()
        print('signup')
        return redirect(url_for('login'))
    print('not signup validate')
    return render_template('signup.html',form=form)

@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user1 = User.query.filter_by(email=email).first()
        print(user1)
        if user1 and user1.password==password:
            print(current_user)
            print(email)
            print(password)
            login_user(user1)
            print('login')
            return redirect(url_for('home1'))
        print('not login')
    print('not login validate')

    return render_template('login.html',form=form)


@app.route('/logout',methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home',methods=['GET','POST'])
def home1():
    return render_template('home.html')

@app.route('/deposit',methods=['GET','POST'])
def deposit1():
    form=DepositForm()
    print(current_user)
    account = Account(current_user.email, current_user.accounts.balance)
    if form.validate_on_submit():
        amount=form.amount.data
        current_user.accounts.balance = account.deposit(amount)
        db.session.commit()
        # print(account.deposit(amount))
        print('deposit')
        return redirect(url_for('home1'))
    print('not validate')
    return render_template('deposit.html',form=form)

@app.route('/withdraw',methods=['GET','POST'])
def withdraw1():
    form = DepositForm()
    print(current_user)
    account = Account(current_user.email, current_user.accounts.balance)
    if form.validate_on_submit():
        amount=form.amount.data
        current_user.accounts.balance = account.withdraw(amount)
        db.session.commit()
        # print(account.withdraw(amount))
        print('withdraw')
        return redirect(url_for('home1'))
    print('not validate')
    return render_template('withdraw.html',form=form)

@app.route('/check',methods=['GET','POST'])
def balance1():
    amount=current_user.accounts.balance
    return render_template('balance.html',amount=amount)

with app.app_context():
    db.create_all()

if __name__ =='__main__':
    app.run(debug=True)