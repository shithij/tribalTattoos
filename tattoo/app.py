import os
from flask import Flask, render_template, request, redirect
import urllib.request
from flask import g
import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate("tribal-tattoo-ae837-firebase-adminsdk-em2bs-4b95dd3eaf.json")
defaultApp = firebase_admin.initialize_app(cred)
db = firestore.client()

salt = "TwinFuries"

app=Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

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
	doc_ref = db.collection(u'events')
	events = doc_ref.get()
	return render_template("events.html")

if __name__ == "__main__":
    app.run(debug=True)