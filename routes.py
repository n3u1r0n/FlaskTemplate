from flask import render_template
from server import app, socketio

@app.route("/")
def root():
    return render_template('main.html')