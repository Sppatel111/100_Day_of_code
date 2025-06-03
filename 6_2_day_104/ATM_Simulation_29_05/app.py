from flask import Flask,render_template,redirect,url_for
from sqlalchemy import String, Integer, Date, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user,login_required
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, SelectField, EmailField
from wtforms.validators import InputRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY']='ERTRTERWTfgdfgedf'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///atm.db'

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# models
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String, nullable=False)
    aadhar: Mapped[int] = mapped_column(Integer, nullable=False)
    account_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    pin: Mapped[int] = mapped_column(Integer, nullable=False)
    balance: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[Date] = mapped_column(DateTime, default=datetime.now())

    transactions = relationship('Transaction', back_populates='users')

    # def deposit(self,amount,id):
    #     Transaction.query.filter_by(id=id,type='deposit').all
    #
    # def withdraw(self):
    #     pass

    def __repr__(self):
        return f'<User {self.id}>'


class Transaction(db.Model):
    __tablename__ = 'transactions'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    type: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    at: Mapped[Date] = mapped_column(DateTime, default=datetime.now())

    users = relationship('User', back_populates='transactions')


# forms
class AddUserForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    account = StringField('Account No.', validators=[InputRequired(), Length(min=11)])
    aadhar = IntegerField('Aadhar No.', validators=[InputRequired()])
    pin = IntegerField('PIN No.', validators=[InputRequired()])
    add= SubmitField('ADD')


class LoginForm(FlaskForm):
    account = StringField('Account No.', validators=[InputRequired(), Length(min=11)])
    pin = IntegerField('PIN No.', validators=[InputRequired()])
    login=SubmitField('Login')

class DepositForm(FlaskForm):
    amount=IntegerField('Amount',validators=[InputRequired()])
    deposit=SubmitField('Deposit')

class WithdrawForm(FlaskForm):
    amount=IntegerField('Amount',validators=[InputRequired()])
    withdraw=SubmitField('Withdraw')

# urls
@app.route('/',methods=['GET','POST'])
def login():
    form=LoginForm()
    account=form.account.data
    pin=form.pin.data
    user1=User.query.filter_by(account_id=account).first()
    if form.validate_on_submit():
        print(user1.pin)
        if user1 and user1.pin == pin:
            login_user(user1)
            print('login')
            return redirect(url_for('home'))
        print('not match requirements')
    print('not validate')
    return render_template('login.html',form=form)
@login_required
@app.route('/logout',methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_required
@app.route('/history',methods=['GET','POST'])
def history():
    user1 = User.query.filter_by(id=current_user.id).first()
    t1=Transaction.query.filter_by(user_id=current_user.id).all()
    return render_template('history.html',t1=t1,user1=user1)

@app.route('/add',methods=['GET','POST'])
def add_user():
    form=AddUserForm()
    if form.validate_on_submit():
        user1=User(
            email=form.email.data,
            account_id=form.account.data,
            aadhar=form.aadhar.data,
            pin=form.pin.data
        )
        db.session.add(user1)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('add_user.html',form=form)

@login_required
@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('home.html')

@login_required
@app.route('/deposit',methods=['GET','POST'])
def deposit():
    form=DepositForm()
    if form.validate_on_submit():
        t1=Transaction(
            type='Deposit',
            amount=form.amount.data,
            user_id=current_user.id
        )
        user1=User.query.filter_by(id=current_user.id).first()
        user1.balance = user1.balance + form.amount.data
        db.session.add(t1)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('deposit.html',form=form)

@login_required
@app.route('/withdraw',methods=['GET','POST'])
def withdraw():
    form = WithdrawForm()
    if form.validate_on_submit():
        t1 = Transaction(
            type='Withdraw',
            amount=form.amount.data,
            user_id=current_user.id
        )
        user1 = User.query.filter_by(id=current_user.id).first()
        if user1.balance > form.amount.data:
            user1.balance = user1.balance - form.amount.data
            db.session.add(t1)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('withdraw.html',form=form)

@login_required
@app.route('/balance',methods=['GET','POST'])
def balance():
    user1=User.query.filter_by(id=current_user.id).first()
    return render_template('balance.html',user1=user1)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
