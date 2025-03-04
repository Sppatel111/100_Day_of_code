from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired,Email,DataRequired,Length
import email_validator
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = 'this-is-my-secret-key'
Bootstrap5(app)

#,Email(message="here the error message")
class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired(), Email(message="Please enter a valid email address.")])
    password = PasswordField('Password', [DataRequired(),Length(min=8, message="Password must be at least 8 characters long.")])
    submit = SubmitField('Log In')

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    email = None
    password = None
    form = LoginForm()

    # if request.method == 'POST':
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email == 'sneha.patel1@aliansoftware.com' and password == '12345678':
            return redirect(url_for("success"))
        else:
            return redirect(url_for('denied'))
    else:
        return render_template('login.html', form=form, email=email, password=password)


@app.route("/denied")
def denied():
    return render_template('denied.html')


@app.route("/success")
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)

# if form.validate_on_submit():
#     email = form.email.data
#     password = form.password.data
#     print(f"Email: {email}, Password: {password}")
#     return redirect(url_for('home'))
# return render_template('login.html', form=form, email=email, password=password)