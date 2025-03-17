from flask_wtf import FlaskForm
from wtforms import StringField,URLField,BooleanField,IntegerRangeField
from wtforms.validators import DataRequired,URL


class AddCafe(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    map_url = URLField("MAP URL",validators=[DataRequired(),URL()]),
    img_url =  URLField("IMG URL",validators=[DataRequired(),URL()]),
    location = StringField("Location",validators=[DataRequired()]),
    has_sockets = BooleanField(" Socket",validators=[DataRequired()]),
    has_toilet = BooleanField("Toilet",validators=[DataRequired()]),
    has_wifi = BooleanField(" wifi",validators=[DataRequired()]),
    can_take_calls = BooleanField(" Take Calls",validators=[DataRequired()]),
    seats = IntegerRangeField("Seats",validators=[DataRequired()]),
    coffee_price = StringField("Coffee Price",validators=[DataRequired()]),