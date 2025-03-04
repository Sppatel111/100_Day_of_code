import os
import smtplib
from flask import Flask, render_template, request
import requests
from config2 import KEY_PASSWORD,EMAIL

EMAIL = EMAIL
PASSWORD = KEY_PASSWORD

app = Flask(__name__)

blog_url = "https://api.npoint.io/929cbb599a79101b2d6f"
blog_response = requests.get(blog_url)
all_post = blog_response.json()


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/')
@app.route('/index.html')
def home():
    return render_template("index.html", posts=all_post)


@app.route('/contact.html', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_msg = f"Subject: New Message!\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,msg=email_msg)


@app.route('/post.html')
def first_post():
    return render_template("post.html")


@app.route('/post/<int:num>')
def find_post(num):
    requested_post = None
    for blog_post in all_post:
        if int(blog_post["id"]) == num:
            requested_post = blog_post

    return render_template("post1.html", posts=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
