import os
from flask import Flask, render_template, request, redirect
import urllib.request
from flask import g
import firebase_admin
from firebase_admin import credentials,firestore
from flask_mail import Mail,Message



cred = credentials.Certificate("tribal-tattoo-ae837-firebase-adminsdk-em2bs-c5b3a1bd5a.json")
defaultApp = firebase_admin.initialize_app(cred)
db = firestore.client()

salt = "TwinFuries"

app=Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tribaltattoont@gmail.com'
app.config['MAIL_PASSWORD'] = 'nottribaltattoo'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def home() : 
	return render_template("index2.html")

@app.route("/about")
def about() : 
	return render_template("about.html")

@app.route("/services")
def services() : 
	return render_template("service3.html")

@app.route("/project")
def project() : 
	return render_template("project.html")

# @app.route("/booking")
# def booking() : 
# 	return render_template("booking.html")

@app.route("/booking",methods=['POST','GET'])
def booking():
	if request.method== 'POST':
		name = request.form['name']
		artist = request.form['artist']
		date = request.form['date']
		time = request.form['time']
		email = request.form['email']
		phNum = request.form['phNum']
		doc_id = email + " " + date
		doc_ref = db.collection(u'appointments').document(doc_id)
		doc_ref.set({
			u'name':name,
			u'contact':phNum,
			u'date':date,
			u'artist':artist,
			u'time':time,
			u'email':email
		})
		message = "Booking Submitted, Check your mail for confirmation"
		return render_template("booking.html", message=message)
	return render_template("booking.html")

@app.route("/blog")
def blog() : 
	return render_template("blog.html")

@app.route("/shop")
def shop() : 
	return render_template("shop.html")

@app.route("/team")
def team() : 
	return render_template("team.html")

@app.route("/portfolio")
def portfolio() : 
	return render_template("team2.html")

@app.route("/contact")
def contact() : 
	return render_template("contact.html")

@app.route("/events")
def events() : 
	doc_ref = db.collection(u'events').get()
	eventList = {}
	for doc in doc_ref:
		eventList[doc.id] = doc.to_dict()
	return render_template("events.html",events=eventList)

@app.route("/register/<event>",methods=['POST','GET'])
def register(event = None) : 
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		phNum = request.form['phNum']
		dob = request.form['dob']
		address = request.form['address']
		# doc_id = email + " " + date
		col_ref = db.collection(u'events').document(event)
		doc_ref = col_ref.collection(u'registrations').document(email)
		doc_ref.set({
			u'name':name,
			u'contact':phNum,
			u'email':email,
			u'dob':dob,
			u'address':address
		})
		msg = Message('Registration Confirmation', sender = 'tribaltattoont@gmail.com', recipients = [email])
		msg.body = "Congratulations, your registration for the event " + event.split(" ")[0] + " on " + event.split(" ")[1] +" has been confirmed"
		mail.send(msg)
		message = "Booking Submitted, Check your mail for confirmation"
		return render_template("register.html", event=event, message=message)
	return render_template("register.html", event = event)

if __name__ == "__main__":
    app.run(debug=True)