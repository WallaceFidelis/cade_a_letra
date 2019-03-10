from flask import render_template
from app import app
from app import db


@app.route("/")
def index():
    return render_template('index.html')