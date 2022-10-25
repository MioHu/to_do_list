import imp
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models.model_user import User

class Share:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.from_id = data['from_id']
        self.to_id = data['to_id']
        self.list_id = data['list_id']
        self.accept = data['accept']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.from_name = ''
        self.to_name = ''
        self.list_name = ''
    


    # class
    @classmethod
    def get_from(cls, data:dict) -> list:
        query = 'SELECT shares.id, from_id, to_id, list_id, accept, shares.created_at, shares.updated_at, users.name AS to_name, lists.name AS list_name FROM shares, users, lists WHERE shares.from_id=%(uid)s AND shares.to_id=users.id AND shares.list_id=lists.id;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return []
        shares = []
        for item in results:
            share = cls(item)
            share.to_name = item['to_name']
            share.list_name = item['list_name']
            shares.append(share)
        return shares
    
    @classmethod
    def get_to(cls, data:dict) -> list:
        query = 'SELECT shares.id, from_id, to_id, list_id, accept, shares.created_at, shares.updated_at, users.name AS from_name, lists.name AS list_name FROM shares, users, lists WHERE shares.to_id=%(uid)s AND shares.from_id=users.id AND shares.list_id=lists.id;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return []
        shares = []
        for item in results:
            share = cls(item)
            share.from_name = item['from_name']
            share.list_name = item['list_name']
            shares.append(share)
        return shares


    # static
    @staticmethod
    def send(data:dict) -> None:
        query = 'INSERT INTO shares (from_id, to_id, list_id) VALUES (%(from_id)s, %(to_id)s, %(list_id)s);'
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @staticmethod
    def receive_accept(data:dict) -> None:
        query1 = 'UPDATE shares SET accept=1 WHERE from_id=%(from_id)s AND to_id=%(to_id)s AND list_id=%(list_id)s;'
        connectToMySQL(DATABASE).query_db(query1, data)
        query2 = 'INSERT INTO user_list VALUES (%(to_id)s, %(list_id)s);'
        connectToMySQL(DATABASE).query_db(query2, data)
        return

    
    @staticmethod
    def receive_reject(data:dict) -> None:
        query = 'UPDATE shares SET accept=0 WHERE from_id=%(from_id)s AND to_id=%(to_id)s AND list_id=%(list_id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def send_validate(data:dict) -> bool:
        is_valid = True
        
        if data['to_id'] == data['from_id']:
            flash('You should pick up another user to send invitation.', 'send')
            is_valid = False

        query1 = 'SELECT COUNT(*) AS cnt FROM shares WHERE from_id=%(from_id)s AND to_id=%(to_id)s AND list_id=%(list_id)s AND accept=10;'
        result1 = connectToMySQL(DATABASE).query_db(query1, data)
        num = result1[0]['cnt']
        if num != 0:
            flash("You've alreday sent an invitation to this user, please wait for a response.", 'send')
            is_valid = False

        return is_valid
    
    @staticmethod
    def find_share_from(data:dict) -> object:
        query = 'SELECT DISTINCT from_id FROM shares WHERE list_id=%(lid)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        from_id = result[0]['from_id']
        user = User.get_one({'uid': from_id})
        return user
    
    @staticmethod
    def find_share_to(data:dict) -> list:
        query = 'SELECT DISTINCT to_id FROM shares WHERE list_id=%(lid)s AND accept=1;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        users = []
        for row in results:
            users.append(User.get_one({'uid': row['to_id']}))
        return users
