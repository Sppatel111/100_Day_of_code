from flask import Flask, render_template, redirect, url_for,jsonify,request
from sqlalchemy import String, Integer, Boolean
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, SubmitField, IntegerField, BooleanField, URLField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
import random


db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ERWERWERfefrwerwe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'

db.init_app(app)


class Base(DeclarativeBase):
    pass


# models
class Cafe(db.Model):
    __tablename__ = 'cafe'
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    map_url: Mapped[str] = mapped_column(String, nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    seats: Mapped[str] = mapped_column(String, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String, nullable=False)


# forms
class AddCafe(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    map_url = URLField('Map Url', validators=[InputRequired()])
    img_url = URLField('Image Url', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    has_sockets = BooleanField('Socket', )
    has_toilet = BooleanField('Toilet')
    has_wifi = BooleanField('Wifi')
    can_take_calls = BooleanField('Take Calls?')
    seats = StringField('Seats', validators=[InputRequired()])
    coffee_price = StringField('Coffee Price', validators=[InputRequired()])
    add = SubmitField('Add')

class Search(FlaskForm):
    location = StringField("Location", validators=[InputRequired()])
    submit = SubmitField("Search")

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add', methods=['GET','POST'])
def add():
    form=AddCafe()
    if form.validate_on_submit():
        c=Cafe(
            name=form.name.data,
        map_url =form.map_url.data ,
        img_url = form.img_url.data,
        location = form.location.data.title(),
        has_sockets = form.has_sockets.data,
        has_toilet =form.has_toilet.data,
        has_wifi = form.has_wifi.data,
        can_take_calls =form.can_take_calls.data ,
        seats = form.seats.data ,
        coffee_price = form.coffee_price.data,

        )
        db.session.add(c)
        db.session.commit()
        return redirect(url_for('home'))
    print('no')
    return render_template('add.html',form=form)

@app.route('/all',methods=['GET','POST'])
def all():
    x = Cafe.query.all()
    return render_template('all.html',x=x)





@app.route('/update/<int:id>',methods=['GET','POST'])
def update_cafe(id):
    cafe=Cafe.query.filter_by(id=id).first()
    form=AddCafe(obj=cafe)
    if form.validate_on_submit():
        cafe.name = form.name.data
        cafe.map_url = form.map_url.data
        cafe.img_url = form.img_url.data
        cafe.location = form.location.data.title()
        cafe.has_sockets = form.has_sockets.data
        cafe.has_toilet = form.has_toilet.data
        cafe.has_wifi = form.has_wifi.data
        cafe.can_take_calls = form.can_take_calls.data
        cafe.seats = form.seats.data
        cafe.coffee_price = form.coffee_price.data
        db.session.commit()
        return redirect(url_for('all'))
    return render_template('update.html',form=form)


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = Search()
    if form.validate_on_submit():
        location = form.location.data.title()
        searched_cafes=Cafe.query.filter_by(location=location).all()
        return render_template('search.html', form=form, x=searched_cafes)
    return render_template('search.html', form=form)

@app.route('/random')
def get_random_cafe():
    all_cafes = Cafe.query.all()
    random_cafe = random.choice(all_cafes)
    return render_template('all.html', x=[random_cafe])

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
