from time import*
from flask import Flask,render_template,request,flash,jsonify
import mysql.connector
from datetime import datetime
from random import randint
from datetime import timedelta
import json
db = mysql.connector.connect(host = "localhost",password = "akash7836",user="root",database = "MyTour")
mycursor = db.cursor()
app = Flask(__name__)
path = "static/tours.json"
with open(path,'r') as file:
    json_data = json.load(file)
def Duration(tour):
    i  = 0
    for data in json_data:
        if(data["name"] != tour):
            i += 1
        else:
            break
    duration = json_data[i]["duration"]
    command = "select TourId from Tour where TourName = %s"
    mycursor.execute(command,(tour,))
    tourid = mycursor.fetchall()
    tourid.append(duration)
    return tourid
def add_booking(tour,tourdate,no_guest,user_id):
    start_date = datetime.strptime(tourdate,"%Y-%m-%d")
    duration = Duration(tour)
    duo = duration[1]
    end_date = start_date+timedelta(days=duo)
    b_time = datetime.now().time()
    command = 'INSERT INTO Bookings (BookingDate, BookingTime, GuestsCount,TourId, TourStartDate, TourEndDate,UserId) VALUES (%s, %s, %s,%s, %s, %s,%s)'
    value = (start_date,b_time,no_guest,duration[0][0],start_date,end_date,int(user_id))
    mycursor.execute(command, value)
    db.commit()
@app.route('/')
def index_page():
    command = 'select*from Bookings'
    mycursor.execute(command)
    myresult = mycursor.fetchall()
    return render_template("index.html",myresult = myresult)
@app.route('/allBookings')
def all_bookings():
    command = 'select*from Bookings'
    mycursor.execute(command)
    myresult = mycursor.fetchall()
    return render_template("allBookings.html",myresult = myresult)

@app.route('/addBookings',methods = ['GET','POST'])
def add_bookings():
    if request.method == 'POST':
        tour = request.form.get("tour")
        tour_date = request.form.get("mydate")
        no_guest = request.form.get("guests")
        user_id = request.form.get("user_id")
        add_booking(tour,tour_date,no_guest,user_id)
        return render_template("addBooking.html",function1 = add_booking)
    return render_template("addBooking.html",function1 = None)

@app.route('/upcoming_bookings')
def upcoming_Tour():
    current_month,current_day,current_year = datetime.now().month,datetime.now().day,datetime.now().year
    real_date = datetime(current_year,current_month,current_day)
    command = 'select*from Bookings where TourStartDate>=CURDATE()'
    mycursor.execute(command)
    myresult = mycursor.fetchall()
    return render_template("upcomingBookings.html",myresult = myresult)

@app.route('/allTour')
def all_tour():
    command = 'select*from Tour'
    mycursor.execute(command)
    myresult = mycursor.fetchall()
    return render_template("tours.html",myresult = myresult)

@app.route('/allusers')
def allUser():
    command = 'select*from User'
    mycursor.execute(command)
    myresult = mycursor.fetchall()
    return render_template("users.html",myresult=myresult)
def delelte_booking(booking_id):
    command = "delete from Bookings where BookingId = %s"
    mycursor.execute(command,(booking_id,))
    db.commit()
@app.route('/deleteBookings',methods = ['GET','POST'])
def delete_bookings():
    if request.method == 'POST':
        bookingId = request.form.get("bookingId")
        delelte_booking(bookingId)
        return render_template("deleteBooking.html",function1 = delelte_booking)
    return render_template("deleteBooking.html",function1 = None)
def modify_booking(booking_id,tour,date,no_guest,user_id):
    # command = "update Bookings set tour = %s"
    start_date = datetime.strptime(date, "%Y-%m-%d")
    duration = Duration(tour)
    duo = duration[1]
    end_date = start_date+timedelta(days=duo)
    tour_id = duration[0][0]
    command = "update Bookings set TourId = %s,TourStartDate = %s,TourEndDate = %s,GuestsCount = %s where BookingId = %s"
    value = (tour_id,start_date,end_date,no_guest,int(booking_id))
    mycursor.execute(command,value)
    db.commit()
@app.route('/modifyBookings',methods = ['GET','POST'])
def modify_bookings():
    if request.method == 'POST':
        booking_id = request.form.get("bookingId")
        tour = request.form.get("tour")
        date = request.form.get("date")
        no_guest = request.form.get("guests")
        user_id = request.form.get("user_id")
        modify_booking(booking_id,tour,date,no_guest,user_id)
        return render_template("modifyBooking.html",function1 = modify_booking)
    return render_template("modifyBooking.html", function1=None)
def modify_users(user,phone_no,email,address,user_id):
    command = 'update User set UserRole = %s, PhoneNumber = %s,Email = %s,Address = %s where UserId=%s'
    value = (user, phone_no, email, address,user_id)
    mycursor.execute(command, value)
    db.commit()
@app.route('/modifyusers',methods = ['GET','POST'])
def modify_user():
    if request.method == 'POST':
        user = request.form.get("Role")
        user_id = request.form.get("booking_id")
        phone_no = request.form.get("phone_no")
        email = request.form.get("email")
        address = request.form.get("address")
        modify_users(user,phone_no,email,address,user_id)
        return render_template("modifyUser.html",function1 = modify_users)
    return render_template("modifyUser.html",function1 = None)
if __name__ == "__main__":
    app.run(debug=True)

