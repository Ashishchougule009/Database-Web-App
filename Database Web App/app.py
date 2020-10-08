from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email # from send_email.py script we are importing send_email function
from sqlalchemy.sql import func


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='postgresql://postgres:postgres123@localhost/height_collector'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__= "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_,height_):
        self.email_ = email_
        self.height_ = height_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST']) #method 'POST' defined in form element in index.html and make sure you give methods in list[]
def success():
    if request.method == "POST":
        email = request.form["email_name"] #gets form element with email_name
        height = request.form["height_name"] #gets form element with email_name
        
        if db.session.query(Data).filter(Data.email_==email).count() == 0: #checks are there any emails in database height_collector that matches the email entered by the user if no then count will be zero and entered email and height will be added to the database 
            data = Data(email,height) # passes email,height to Data class
            db.session.add(data)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height,1)
            count = db.session.query(Data.height_).count()
            send_email(email,height, average_height, count) #send_email is a function defined in send_email.py script which is used to send mail
            return render_template("success.html")
    return render_template("index.html", text = "Seems like we've got something from that email address already!")

if __name__ == '__main__':
    app.debug= True
    app.run()