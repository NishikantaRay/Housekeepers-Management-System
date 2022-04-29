from flask import Flask, render_template, request
import pandas as p
import random
from tkinter import messagebox
import csv
userno=1
app = Flask(__name__)
import smtplib
sender_mail=""
sender_pass=""
def sendotp(useremail):
    global sender_mail
    global sender_pass
    a = random.randint(1000, 10000)
    # with smtplib.SMTP("smtp.gmail.com", 587) as connect:
    #     connect.starttls()
    #     connect.login(user=sender_mail, password=sender_pass)
    #     connect.sendmail(from_addr=sender_mail, to_addrs=username, msg=f"Your confirmation password is \n\n:{a}")
    print(a)
    return a
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
    with open("data.csv", "r") as data_file:
        data = csv.reader(data_file)
        for row in data:
            if email == row[0] and password == row[1]:
                return render_template("home.html")
        return render_template("login.html",wrongpass=1,userexists=0)

@app.route("/otp",methods=["POST"])
def otp():
    username = request.form["username"]
    password= request.form["pass"]
    with open("data.csv", "r") as data_file:
        data = csv.reader(data_file)
        for row in data:
            if username == row[0] :
                return render_template("login.html",wrongpass=0,userexists=1)
    a = sendotp(username)
    return render_template("otp.html",username=username,password=password,otp=str(a),updatepass=0)
@app.route("/login-otp",methods=["POST"])
def loginotp():
    username = request.form["username"]
    with open("data.csv", "r") as data_file:
        data = csv.reader(data_file)
        for row in data:
            if username == row[0] :
                a = sendotp(username)
                return render_template("updatepassword.html",otp=str(a),username=username)
    return render_template("login.html", wrongpass=0, userexists=2)

@app.route("/updatepass",methods=["POST"])
def upass():
    data=[]
    username = request.form["username"]
    password = request.form["pass"]
    with open("data.csv", "r") as data_file:
        csvdata = csv.reader(data_file)
        for row in csvdata:
            if username == row[0] :
                row[1]=password
            data.append(row)
    with open("data.csv", "w",) as data_file:
        writer = csv.writer(data_file ,lineterminator='\n')
        for i in data:
            writer.writerow(i)
    return render_template("home.html")

@app.route("/createacc",methods=["POST"])
def cacc():
    data=[]
    username = request.form["username"]
    password = request.form["pass"]
    with open("data.csv", "r") as data_file:
        csvdata = csv.reader(data_file)
        for row in csvdata:
            data.append(row)
        data.append([username,password,"",{}])
    with open("data.csv", "w",) as data_file:
        writer = csv.writer(data_file ,lineterminator='\n')
        for i in data:
            writer.writerow(i)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
