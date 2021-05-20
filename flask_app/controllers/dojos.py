from flask import  render_template, request, redirect
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers import dojos, ninjas
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app

@app.route('/dojos')
def homepage():
    dojos = Dojo.get_all()
    return render_template('index.html', dojos = dojos)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    user_input = request.form
    Dojo.create_dojo(user_input)
    return redirect('/')

@app.route('/dojo/show/<int:id>')
def show_one_dojo(id):
    dojo = Dojo.get_one(id)
    ninjas = Ninja.get_all_by_dojo(id)
    return render_template('ninjas.html', dojo = dojo, ninjas = ninjas)