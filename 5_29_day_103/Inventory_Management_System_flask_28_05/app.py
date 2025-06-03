from flask import Flask, redirect, render_template, url_for
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, ForeignKeyConstraint,and_
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user,current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, EmailField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Email
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DFGFGSDFASDF'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

migrate = Migrate(app, db)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# models

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f'<User {self.id}>'


class Product(db.Model):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, default=0)

    orders = relationship('Order', back_populates='products')


class Order(db.Model):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('products.id', ondelete="CASCADE"))
    quantity: Mapped[int] = mapped_column(Integer,default=0, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer)
    __table_args__ = (ForeignKeyConstraint
                      (['user_id'], ['users.id'], ondelete='CASCADE'),
                      )

    products = relationship('Product', back_populates='orders')


# forms
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[Email(), InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    login = SubmitField('Login')


class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[Email(), InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    Signup = SubmitField('Signup')


class AddProduct(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    price = IntegerField('Price', validators=[InputRequired()])
    stock = IntegerField('Stock', validators=[InputRequired()])
    add = SubmitField('ADD')


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    email = form.email.data
    password = form.password.data
    user1 = User.query.filter_by(email=email).first()
    if form.validate_on_submit():
        if user1 and user1.password == password:
            login_user(user1)
            print('login')
            return redirect(url_for('home'))
        print('incorrect')
    print('not validate')
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user1 = User(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user1)
        db.session.commit()
        print('signup')
        return redirect(url_for('login'))
    print('not validate')
    return render_template('signup.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home', methods=['GET', 'POST'])
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)


@app.route('/buy/<int:id>', methods=['GET', 'POST'])
def view_product(id):
    product1 = Product.query.filter_by(id=id).first()
    cart = Order.query.filter(and_(Order.user_id == current_user.id, Order.product_id == id)).first()
    return render_template('view_product.html',product1=product1,cart=cart)


@app.route('/add_cart/<int:id>', methods=['GET', 'POST'])
def add_cart(id):
    cart = Order.query.filter(and_(Order.user_id == current_user.id, Order.product_id == id)).first()
    if cart:
        cart.quantity = cart.quantity + 1
    else:
        item = Order(
            product_id=id,
            quantity= 1,
            user_id=current_user.id
        )
        db.session.add(item)
    db.session.commit()
    return redirect(url_for('view_product',id=id))

@app.route('/remove_cart/<int:id>', methods=['GET', 'POST'])
def remove_cart(id):
    cart = Order.query.filter(and_(Order.user_id == current_user.id, Order.product_id == id)).first()
    if cart and cart.quantity > 0:
        cart.quantity = cart.quantity - 1
    elif cart.quantity == 0:
        db.session.delete(cart)
    else:
        print('not in cart')
    db.session.commit()
    return redirect(url_for('view_product', id=id))

@app.route('/checkout/<int:id>', methods=['GET','POST'])
def checkout(id):
    product1 = Product.query.filter_by(id=id).first()
    cart = Order.query.filter(and_(Order.user_id == current_user.id, Order.product_id == id)).first()
    product1.stock = product1.stock - cart.quantity
    db.session.commit()
    return render_template('checkout.html',product1=product1,cart=cart)

@app.route('/cart-history', methods=['GET', 'POST'])
def history():
    pro1 = Product.query.all()
    cart=Order.query.filter_by(user_id=current_user.id).all()
    return render_template('cart_history.html',cart=cart,pro1=pro1)

# admin
@app.route('/admin', methods=['GET', 'POST'])
def a_products():
    products = Product.query.all()
    return render_template('a_products.html', products=products)


@app.route('/admin/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    pro = Product.query.filter_by(id=id).first()
    form = AddProduct(obj=pro)
    if form.validate_on_submit():
        pro.name = form.name.data
        pro.price = form.price.data
        pro.stock = form.stock.data
        db.session.commit()
        return redirect(url_for('a_products'))
    return render_template('a_update.html', form=form, pro=pro)


@app.route('/admin/add', methods=['GET', 'POST'])
def add_products():
    form = AddProduct()
    if form.validate_on_submit():
        pro = Product(
            name=form.name.data,
            price=form.price.data,
            stock=form.stock.data
        )
        db.session.add(pro)
        db.session.commit()
        return redirect(url_for('a_products'))
    return render_template('add_product.html', form=form)

@app.route('/admin/orders/<int:id>', methods=['GET', 'POST'])
def all_orders(id):
    orders=Order.query.filter_by(product_id=id).all()
    return render_template('all_orders.html',orders=orders)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
