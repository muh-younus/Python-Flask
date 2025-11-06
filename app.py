from flask import Flask,render_template,request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///user.db"
db = SQLAlchemy(app)

class user(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable = False)
    password = db.Column(db.String(40), nullable = False)
    datetime = db.Column(db.DateTime, default = datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    all_user = user.query.all()
    return render_template('index.html', all_user = all_user)

@app.route("/about")
def about():
    return render_template('about.html', head='About section')
@app.route("/contact")
def contact():
    return "My contact  Page"
@app.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        new_user= user(
            username = username,
            password = password
        )
        db.session.add(new_user)
        db.session.commit()
        print(f"Username: {username}, Password: {password}")
        return redirect(url_for('register'))

    return render_template('register.html')

@app.route("/update/<index>",methods=['GET','POST'])
def update(index):
    User = user.query.filter_by(sno=index).first()
    if request.method == 'POST':
        username1=request.form['username2']
        password1 = request.form['password2']
        User.username = username1
        User.password = password1
        db.session.add(User)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update.html', user = User)
@app.route("/delete/<index>",methods=['GET','POST'])
def delete(index):
    User = user.query.filter_by(sno=index).first()
    db.session.delete(User)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)