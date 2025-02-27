from flask import Flask ,render_template

app=Flask(__name__)

@app.route("/home")
def home():
    x="this is home page"
    return render_template("home.html",message=x)

if __name__ == "__main__":
    app.run()
