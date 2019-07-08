import os
from flask import Flask, render_template, request, redirect
import urllib.request
from flask import g
# from firebase import firebase
# import firebase from '../js/firebaseInit'
# import { firestore } from 'firebase';

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

@app.route("/booking")
def booking() : 
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
	return render_template("events.html")

if __name__ == "__main__":
    app.run(debug=True)