from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import re
import sys
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)
db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{}:{}@{}/{}".format(db_username, db_password,db_host ,db_name )
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
def create_tables():
    with app.app_context():
        db.create_all()
create_tables()  
@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"
@app.route('/add_user',  methods=['GET','POST'],strict_slashes=False)
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        user = User(name=name,email=email)
        try:
            with app.app_context():
                db.session.add(user)
                db.session.commit()
                return "User added successfully!"
        except Exception as error:
            return str(error.orig) + " for parameters" + str(error.params)
                    
    return render_template('add_user.html')
@app.route('/users', strict_slashes=False)
def users():
    users = User.query.all()
    return render_template('users.html',users=users)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
    