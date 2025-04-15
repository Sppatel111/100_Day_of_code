from flask import Flask,render_template,request,redirect,url_for
from datetime import datetime
app=Flask(__name__)

entries=[]
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html',entries=entries)

@app.route('/add',methods=['GET','POST'])
def add_entry():
    content=request.form.get('content')
    if content:
        timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        entries.append({'content': content, 'timestamp': timestamp})

    return redirect(url_for('home'))


if __name__ =="__main__":
    app.run(debug=True)
