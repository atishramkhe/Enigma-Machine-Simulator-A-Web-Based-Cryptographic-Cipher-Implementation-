import os

from cs50 import SQL
import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

from enigma import encryption, apology

from datetime import datetime

# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///rotorstable.db")

# Loading databases of rotors and reflectors wiring, name and model
models = db.execute("SELECT DISTINCT model FROM rotors")
rotors_db = db.execute("SELECT rotor_name, model, wiring FROM rotors")
reflectors_db = db.execute("SELECT reflector_name, wiring FROM reflectors")

# Creating dictionaries for reflectors and rotors for easier use in python
reflectors = {}
for i in reflectors_db:
    reflectors.update({i["reflector_name"]: i["wiring"]})

rotors = {}
for i in rotors_db:
    rotors.update({i["rotor_name"]: i["wiring"]})


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        plaintext = request.form.get("plaintext")
        if not plaintext:
            return apology("No plaintext")

        rotors_choice = [request.form.get("rotor1"), request.form.get(
            "rotor2"), request.form.get("rotor3")]
        rotor1pos = int(request.form.get("rotor1pos"))
        rotor2pos = int(request.form.get("rotor2pos"))
        rotor3pos = int(request.form.get("rotor3pos"))
        rotors_pos_ = [rotor1pos, rotor2pos, rotor3pos]
        if not rotors_choice:
            return apology("No rotors chosen")
        for i in range(len(rotors_pos_)):
            if rotors_pos_[i] < 1 or rotors_pos_[i] > 26:
                return apology("Rotors positions outside limit")

        reflector_type = request.form.get("reflector")
        if not reflector_type:
            return apology("No reflector chosen")
        print(reflectors.keys())
        if reflector_type not in reflectors.keys():
            return apology("Reflector not in list")

        ciphertext = encryption(plaintext, rotors_choice, rotors_pos_,
                                reflector_type, rotors, reflectors)
        return render_template("index.html", plaintext=plaintext, ciphertext=ciphertext, reflectors=reflectors_db, rotors=rotors_db, rotor1pos=rotor1pos, rotor2pos=rotor2pos, rotor3pos=rotor3pos, rotors_choice=rotors_choice, reflector_type=reflector_type)
    else:
        # Intialising rotors positions to 1
        rotor1pos = 1
        rotor2pos = 1
        rotor3pos = 1
        return render_template("index.html", reflectors=reflectors_db, rotors=rotors_db, rotor1pos=rotor1pos, rotor2pos=rotor2pos, rotor3pos=rotor3pos)
