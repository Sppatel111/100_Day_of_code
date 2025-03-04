from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
# "https://api.themoviedb.org/3/movie"
# https://developers.themoviedb.org/3/search/search-movies
MOVIE_DB_API_KEY = "ce4ade9483f83239666817be95620239"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


# CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[int] = mapped_column(String(500), unique=True, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class MovieRateForm(FlaskForm):
    rating = StringField('Your rating out of 10. eg. 7.5')
    review = StringField('Your Review')
    submit = SubmitField('Done')


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie))
    all_movie = result.scalars().all()
    return render_template("index.html", movies=all_movie)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        try:
            response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
            data = response.json()["results"]
            return render_template("select.html", options=data)
        except requests.exceptions.ConnectionError:
            return "connection error."
    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_Key": MOVIE_DB_API_KEY})
        data = response.json()
        print(data)

        new_movie = Movie(
            title=data.get("title"),
            year=data.get("release_date","Unknown").split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data.get('poster_path')}",
            description=data.get("overview")
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))

@app.route("/movie/<int:id>")
def movie_details(id):
    movie_api_url = f"{MOVIE_DB_INFO_URL}/{id}"
    response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY})
    data = response.json()

    # Check if the movie data is valid
    if not data or 'status_code' in data and data['status_code'] != 200:
        return "Movie not found", 404

    return render_template("movie_detail.html", movie=data)
@app.route("/edit", methods=['GET', 'POST'])
def rate_movie():
    form = MovieRateForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('edit.html', movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()

