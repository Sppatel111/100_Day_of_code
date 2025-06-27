# Online Shopping Cart
#
# Implement Product, Cart, and User classes with cart operations (add, remove, checkout).

from flask import Flask, redirect, render_template, url_for,request,jsonify
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, ForeignKeyConstraint,and_
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin,current_user
from wtforms import StringField, SelectField, SubmitField, EmailField, PasswordField, TextAreaField,IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import Email, InputRequired
import stripe

stripe.api_key = 'sk_test_51Re6wwRmoCZ9fJ30Sdz9EbYy8EFTgBqLOWdeQ33JkbDt6ln7PtkkXfiaaEzMgzDnch1FojgW5MjMq492dXKaX3nL00kKFIuvLW'

YOUR_DOMAIN = 'http://127.0.0.1:5000'
# stripe.api_key='https://api.stripe.com'

# uri=request.get('https://api.stripe.com')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TYTYT4TWERTERSZEAEWR'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51Re6wwRmoCZ9fJ30BdvM1TcAiIQpL5LDFkNTkbRhrCAmR07aRTQ0G2OGMxHVB81BTVuHey0e8v4FAOYzrjSpk3cl00C3jAQzmx'
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51Re6wwRmoCZ9fJ30Sdz9EbYy8EFTgBqLOWdeQ33JkbDt6ln7PtkkXfiaaEzMgzDnch1FojgW5MjMq492dXKaX3nL00kKFIuvLW'


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

db.init_app(app)
login_manager=LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f'<User {self.id}>'


class Product(db.Model):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f'<Product {self.id}>'

    carts = relationship('Cart', back_populates='products')


class Cart(db.Model):
    __tablename__ = 'carts'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('products.id', ondelete="CASCADE"))
    customer_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
    quantity: Mapped[int] = mapped_column(Integer, default=0, nullable=False)


    __table_args__ = (ForeignKeyConstraint
                      (['product_id'], ['products.id'], ondelete='CASCADE'),
                      )

    products = relationship('Product', back_populates='carts')

    # def __init__(self, id, product_id, customer_id, quantity):
    #     self.id = id
    #     self.product_id = product_id
    #     self.customer_id = customer_id
    #     self.quantity = quantity

    def add(self, pid, cid, q):
        cart = Cart.query.filter_by(product_id=pid, customer_id=cid).first()
        if cart:
            cart.quantity = q+1
        else:
            item = Cart(
                product_id=pid,
                customer_id=cid,
                quantity= q+1
                )
            db.session.add(item)
        db.session.commit()


    def remove(self,id,q):
        cart = Cart.query.filter_by(id=id).first()


        if cart and cart.quantity > 0:
            cart.quantity = q-1
        elif cart.quantity == 0:
            db.session.delete(cart)
        db.session.commit()

    def total(self,q,price):
        return q * price

    def checkout(self,q,price):
        return redirect((url_for('')))



# forms
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[Email(), InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    login = SubmitField('Login')


class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[Email(), InputRequired()])
    address = TextAreaField('Address', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    Signup = SubmitField('Signup')

class AddProduct(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    price=IntegerField('Price',default=500)
    status=SelectField('Status',choices=[('available','Available'),('not-available','Not-available')])
    add=SubmitField('Add')

class UpdateProduct(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    price=IntegerField('Price',default=500)
    status=SelectField('Status',choices=[('available','Available'),('not-available','Not-available')])
    add=SubmitField('Update')




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
            address=form.address.data,
            password=form.password.data
        )
        db.session.add(user1)
        db.session.commit()
        print('signup')
        return redirect(url_for('login'))
    print('not validate')
    return render_template('signup.html',form=form)

@app.route('/logout',methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home', methods=['GET', 'POST'])
def home():
    pro1 = Product.query.all()
    return render_template('home.html', pro1=pro1)

@app.route('/view/<int:id>', methods=['GET', 'POST'])
def view_product(id):
    product1=Product.query.filter_by(id=id).first()
    cart=Cart.query.filter(and_(Cart.customer_id == current_user.id, Cart.product_id == id)).first()
    return render_template('view_product.html',product1=product1,cart=cart)

@app.route('/add_cart/<int:id>', methods=['GET', 'POST'])
def add_cart(id):
    cart = Cart.query.filter(and_(Cart.customer_id == current_user.id, Cart.product_id == id)).first()
    # cart = Cart.query.filter_by(customer_id=current_user.id, product_id=id).first()
    c = Cart()
    if cart:
        c.add(id,current_user.id,cart.quantity)
    else:
        c.add(id, current_user.id, 0)
    return redirect(url_for('view_product',id=id))
    # return redirect(url_for('home'))

@app.route('/remove_cart/<int:id>', methods=['GET', 'POST'])
def remove_cart(id):
    print(current_user)
    # cart = Cart.query.filter_by(customer_id=current_user.id, product_id=id).first()
    # cart = Cart.query.filter_by(id=id).first()
    cart = Cart.query.filter(and_(Cart.customer_id == current_user.id, Cart.product_id == id)).first()
    c = Cart()
    if cart:
        print(cart.id)
        c.remove(cart.id,cart.quantity)
        # c.remove(id,current_user.id,cart.quantity)
        print('yes')
    else:
        print('not in cart')
    return redirect(url_for('view_product', id=id))
    # return redirect(url_for('history'))


# @app.route('/create-payment-intent', methods=['POST'])
# def create_payment():
#     data = request.get_json()
#     payment_method_id = data['payment_method_id']
#     total_amount = data['amount']
#
#     stripe.api_key = app.config['STRIPE_SECRET_KEY']
#     try:
#         intent = stripe.PaymentIntent.create(
#             amount=total_amount,
#             currency='usd',
#             payment_method=payment_method_id,
#             confirmation_method='manual',
#             confirm=True,
#             return_url='https://yourdomain.com/return'
#         )
#         return jsonify({'success': True})
#     except Exception as e:
#         return jsonify({'error': str(e)})

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, price_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)
@app.route('/checkout/<int:id>', methods=['GET', 'POST'])
def checkout(id):
    product1 = Product.query.filter_by(id=id).first()
    cart = Cart.query.filter(and_(Cart.customer_id == current_user.id, Cart.product_id == id)).first()

    if cart and cart.quantity > 0:
        total_amount = product1.price * cart.quantity
        return render_template('checkout.html', product1=product1, cart=cart,
                               stripe_public_key=app.config['STRIPE_PUBLIC_KEY'],
                               total_amount=total_amount)
    else:
        return redirect(url_for('view_product', id=id))



@app.route('/cart-history', methods=['GET', 'POST'])
def history():
    pro1 = Product.query.all()
    cart=Cart.query.filter_by(customer_id=current_user.id).all()
    return render_template('cart_history.html',cart=cart,pro1=pro1)

@app.route('/h-view/<int:id>', methods=['GET', 'POST'])
def view_history_product(id):
    product1=Product.query.filter_by(id=id).first()
    cart=Cart.query.filter(and_(Cart.customer_id == current_user.id, Cart.product_id == id)).first()
    return render_template('view_history_product.html',product1=product1,cart=cart)

 #admin
@app.route('/all',methods=['GET','POST'])
def all():
    pro1 = Product.query.all()
    return render_template('admin_all.html', pro1=pro1)

@app.route('/add',methods=['GET','POST'])
def add():
    form=AddProduct()
    if form.validate_on_submit():
        product1=Product(
            name=form.name.data,
            status=form.status.data,
            price=form.price.data
        )
        db.session.add(product1)
        db.session.commit()
        return redirect(url_for('all'))

    return render_template('add_product.html',form=form)

@app.route('/update/<int:id>',methods=["GET","POST"])
def update(id):
    product1=Product.query.filter_by(id=id).first()

    form=UpdateProduct(obj=product1)
    if form.validate_on_submit():
        product1.name=form.name.data
        product1.status=form.status.data
        product1.price=form.price.data
        db.session.commit()
        return redirect(url_for('all'))
    return render_template('update_product.html',form=form,product1=product1)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
