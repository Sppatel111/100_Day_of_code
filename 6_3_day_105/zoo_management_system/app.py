# Zoo Management System
# Class hierarchy with Animal, Mammal, Bird, etc., using polymorphism to define behaviors.

from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from wtforms import StringField, SelectField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SECRET_KEY'] = 'FERewrwerwr'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zoo_management.db'


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)
migrate=Migrate()
migrate.init_app(app,db)
# models
class Animal(db.Model):
    __tablename__ = 'animals'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    species: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    sound: Mapped[str] = mapped_column(String, nullable=False, default="some sound")
    status:Mapped[str]=mapped_column(String,default='Present',nullable=True)
    __mapper_args__ = {
        'polymorphic_identity': 'animal',
        'polymorphic_on': type,
        'with_polymorphic': '*'
    }

    def __init__(self, name,species,type,sound='some sound'):
        self.name = name
        self.species=species
        self.type=type
        self.sound=sound

    def make_sound(self):
        return f'{self.name} some sounds'


class Mammal(Animal):
    __mapper_args__ = {
        'polymorphic_identity': 'mammal',
    }

    def make_sound(self):
        return f'{self.name}{self.species} Roaring'


class Bird(Animal):
    __mapper_args__ = {
        'polymorphic_identity': 'bird',
    }

    def make_sound(self):
        return f'{self.name }{self.species} Chirping'


# forms
class AddAnimals(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired()])
    type = SelectField('Type', choices=[('mammal', 'mammal'), ('bird', 'bird')])
    add = SubmitField('Add')


# urls
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddAnimals()
    if form.validate_on_submit():
        print('validate')
        type = form.type.data
        print(type)
        if type == 'mammal':
            animal = Mammal(form.name.data,form.species.data,'mammal')
        elif type == 'bird':
            animal = Bird(form.name.data,form.species.data,'bird')
        else:
            animal = Animal()
        a1 = Animal(
            name=form.name.data,
            species=form.species.data,
            type=form.type.data,
            sound=animal.make_sound(),
            status='Present'
        )
        db.session.add(a1)
        db.session.commit()
        return redirect(url_for('view'))
    return render_template('add.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def view():
    a1=Animal.query.all()
    return render_template('view.html',a1=a1)

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    a=Animal.query.filter_by(id=id).first()
    if a.status =='Present':
        a.status ='Not-Present'
    elif a.status == 'Not-Present':
        a.status='Present'
    else:
        a.status='Present'
    db.session.commit()
    return redirect(url_for('view'))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
