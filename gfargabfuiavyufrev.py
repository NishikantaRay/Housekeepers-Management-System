from flask import Flask, render_template, request
import pandas as p
import random
from tkinter import messagebox
import csv
userno=1
app = Flask(__name__)
import smtplib
sender_mail="arpitmishra.dkl@gmail.com"
sender_pass="THEundertaker?"
@app.route('/')
def root():
    return render_template("index.html")
@app.route('/home')
def home():
    return render_template("home.html")
@app.route('/login')
def get_all_posts():
    return render_template("login.html",wrongpass=0,userexists=0)

@app.route("/Authentication", methods=["POST"])
def receive_data():
    email = request.form["username"]
    password = request.form["pass"]
    new_data = {
            "E-mail": email,
            "Password": password,
            "contact" : "",
            "services" : {}
        }
    with open("data.csv", "r") as data_file:
        data = csv.reader(data_file)
        for row in data:
            if new_data["E-mail"] == row[0] and new_data["Password"] == row[1]:
                return render_template("home.html")

        return render_template("login.html",wrongpass=1,userexists=0)

@app.route("/otp",methods=["POST"])
def otp():
    username = request.form["username"]
    with open("data.csv", "r") as data_file:
        data = csv.reader(data_file)
        for row in data:
            if username == row[0] :
                return render_template("login.html",wrongpass=0,userexists=1)
    a = random.randint(1000, 10000)
    # with smtplib.SMTP("smtp.gmail.com", 587) as connect:
    #     connect.starttls()
    #     connect.login(user=sender_mail, password=sender_pass)
    #     connect.sendmail(from_addr=sender_mail, to_addrs=username, msg=f"Your confirmation password is \n\n:{a}")
    print(a)
    return render_template("otp.html",otp=str(a),updatepass=0)
@app.route("/lotp",methods=["POST"])
def loginotp():
    username = request.form["username"]
    with open("data.csv", "r") as data_file:
        data = csv.reader(data_file)
        for row in data:
            if username == row[0] :
                a = random.randint(1000, 10000)
                # with smtplib.SMTP("smtp.gmail.com", 587) as connect:
                #     connect.starttls()
                #     connect.login(user=sender_mail, password=sender_pass)
                #     connect.sendmail(from_addr=sender_mail, to_addrs=username, msg=f"Your confirmation password is \n\n:{a}")
                print(a)
                return render_template("otp.html",otp=str(a),updatepass=1)
    return render_template("login.html", wrongpass=0, userexists=2)

@app.route("/updatepass",methods=["POST"])
def upass():
    return render_template("updatepassword.html")
if __name__ == "__main__":
    app.run(debug=True)
