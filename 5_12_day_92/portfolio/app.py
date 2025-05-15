from flask import Flask,render_template

app=Flask(__name__)

@app.route('/project')
def home():
    return render_template("home.html")

@app.route('/')
def index():
    return render_template('index.html')
def project_detail():
    return render_template('')

if __name__=="__main__":
    app.run(debug=True)

#https://mdbootstrap.com/docs/standard/