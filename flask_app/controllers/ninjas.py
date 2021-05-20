from flask import  render_template, request, redirect
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers import dojos, ninjas
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app

@app.route('/ninja/add')
def add_ninja():
    dojos = Dojo.get_all()
    return render_template('newninja.html', dojos = dojos)

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    user_input = request.form
    Ninja.new_ninja(user_input)
    return redirect('/dojo/show/' + str(user_input['dojo_id']))