from flask import  render_template, request, redirect
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers import dojos, ninjas
from flask_app import app

@app.route('/')
def index():
    return redirect('/dojos')