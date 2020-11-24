from flask import render_template, redirect, url_for, request, jsonify
from application import app
from application.models import Animals
import random

@app.route('/')
def index():
    return render_template("index.html")
    random_animal = random.choice(list(Animals.items()))
