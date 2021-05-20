from flask_app.config.mysqlconnection import connectToMySQL

db = 'dojos_and_ninjas'

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #C
    @classmethod
    def create_dojo(cls, user_input):
        mysql = connectToMySQL(db)
        query = "INSERT INTO dojos (name) VALUE (%(name)s)"
        data = {
            'name' : user_input['name']
        }
        return mysql.query_db(query, data)

    #R
    @classmethod
    def get_all(cls):
        mysql = connectToMySQL(db)
        query = 'SELECT * FROM dojos;'
        dojos_from_db = mysql.query_db(query)
        dojos = []
        for dojo in dojos_from_db:
            dojos.append(cls(dojo))
        return dojos

    @classmethod 
    def get_one(cls, id):
        mysql = connectToMySQL(db)
        query = 'SELECT * FROM dojos WHERE id = %(id)s'
        data = {
        'id' : id
        }
        dojo = mysql.query_db(query, data)[0]
        return dojo