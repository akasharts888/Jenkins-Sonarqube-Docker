from flask import Flask,render_template,request,flash
import requests
from jinja2 import *
import mysql.connector
db = mysql.connector.connect(host = "localhost",password = "akash7836",user="root",database = "user")
mycursor = db.cursor()

app = Flask(__name__,template_folder="My_Practice/templates")
app.secret_key = 'abc'
name = ""
roll = 0
def show_data():
    pass
def add_new_user(name,roll):
    add = "insert into student(name,roll) values(%s,%s)"
    mycursor.execute(add,(name,roll))
    db.commit()
@app.route("/",methods = ['GET','POST'])
def hell_world():
    command = "select*from student"
    mycursor.execute(command)
    myresult = mycursor.fetchall()
    name = request.form.get("Name")
    roll = request.form.get("Roll")
    if(name == "" or roll == ""):
        flash("")
        print(name,roll)
        pass
    else:
        add_new_user(name,roll)
    return render_template("practice_page.html", size=len(myresult), data=myresult)

if __name__ == "__main__":
    app.run(debug=True)
