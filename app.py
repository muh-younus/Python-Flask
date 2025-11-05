from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html', head='About section')
@app.route("/contact")
def contact():
    return "My contact  Page"
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        print(f"Username: {username}, Password: {password}")
    
    return render_template('login.html ')

if __name__ == "__main__":
    app.run(debug=True)