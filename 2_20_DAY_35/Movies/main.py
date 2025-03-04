from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import csv

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

def load_movies_from_csv():
    movies = []
    with open('csv_file.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movies.append({
                'id': row["Ranking"],
                'title': row['Title'],
                'year': row['Release Date'],
                'description': row['Overview'],
                'rating': row['Rating'],
                'review': row['Review'],
                'ranking':row['Ranking']
            })
    return movies

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
        movies = load_movies_from_csv()
        # Filter movies based on the title
        filtered_movies = [movie for movie in movies if movie_title.lower() in movie['title'].lower()]
        return render_template("select.html", options=filtered_movies)

    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_id = request.args.get("id")
    movies = load_movies_from_csv()
    movie = next((m for m in movies if m['id'] == movie_id), None)

    if movie:
        new_movie = Movie(
            title=movie['title'],
            year=movie['year'],
            img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg",
            description=movie['description'],
            rating=movie['rating'],
            review=movie['review'],
            ranking=movie['ranking']
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home", id=new_movie.id))
    return redirect(url_for("add"))


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

