from flask_app.config.mysqlconnection import connectToMySQL

db = 'dojos_and_ninjas'

class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #C
    @classmethod
    def new_ninja(cls, user_input):
        mysql = connectToMySQL(db)
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"
        data = {
            'first_name' : user_input['first_name'],
            'last_name' : user_input['last_name'],
            'age' : user_input['age'],
            'dojo_id' : user_input['dojo_id']
        }
        mysql.query_db(query, data)
        return 

    #R
    @classmethod 
    def get_all_by_dojo(cls, id):
        mysql = connectToMySQL(db)
        query = 'SELECT * FROM ninjas WHERE dojo_id = %(id)s'
        data = {
        'id' : id
        }
        ninjas_from_db = mysql.query_db(query, data)
        ninjas = []
        for ninja in ninjas_from_db:
            ninjas.append(cls(ninja))
        return ninjas