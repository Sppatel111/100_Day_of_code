import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from forms import AddCafe
app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SECRET_KEY']='rwertwetwetwerwer'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)

    return jsonify(cafe={
        "id":random_cafe.id,
        "name":random_cafe.name,
        "map_url":random_cafe.map_url,
        "img_url":random_cafe.img_url,
        "location":random_cafe.location,
        "seats":random_cafe.seats,
        "has_toilet":random_cafe.has_toilet,
        "has_wifi":random_cafe.has_wifi,
        "has_sockets":random_cafe.has_sockets,
        "can_take_calls":random_cafe.can_take_calls,
        "coffe_price":random_cafe.coffee_price
    })

@app.route("/all")
def all_get():
    result=db.session.execute(db.select(Cafe))
    all_cafes=result.scalars().all()

    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

#search?loc=London Bridge
@app.route("/search")
def search_by_location():
    query_location=request.args.get("loc")
    result=db.session.execute(db.select(Cafe).where(Cafe.location==query_location))
    all_cafes=result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found":"sorry, we don't have cafe at that location"}),404

# HTTP POST - Create Record
# @app.route("/add", methods=["GET","POST"])
# def post_new_cafe():
#     if request.form=='POST':
#         new_cafe = Cafe(
#             name=request.form.get("name"),
#             map_url=request.form.get("map_url"),
#             img_url=request.form.get("img_url"),
#             location=request.form.get("loc"),
#             has_sockets=bool(request.form.get("sockets")),
#             has_toilet=bool(request.form.get("toilet")),
#             has_wifi=bool(request.form.get("wifi")),
#             can_take_calls=bool(request.form.get("calls")),
#             seats=request.form.get("seats"),
#             coffee_price=request.form.get("coffee_price"),
#         )
#         db.session.add(new_cafe)
#         db.session.commit()
#         return jsonify(response={"success": "Successfully added the new cafe."})
#     return render_template('add.html')
@app.route("/add",methods=['GET','POST'])
def post_new_cafe():
    form=AddCafe()
    if form.validate_on_submit():
        new_cafe=Cafe(
            name=request.form.get("name"),
            map_url = request.form.get("map_url"),
            img_url = request.form.get("img_url"),
            location = request.form.get("location"),
            has_sockets = bool(request.form.get("has_sockets")),
            has_toilet = bool(request.form.get("has_toilet")),
            has_wifi = bool(request.form.get("has_wifi")),
            can_take_calls = bool(request.form.get("can_take_calls")),
            seats = request.form.get("seats"),
            coffee_price = request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"Success":"Successfully added new cafe."})
    return render_template('add.html',form=form)

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["GET","PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})

# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>",methods=["Delete"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")
    if api_key == "TopSecretAPIKey":
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403



if __name__ == '__main__':
    app.run(debug=True)
