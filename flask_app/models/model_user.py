from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.pw = data['pw']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    

    # class
    @classmethod
    def get_one(cls, data:dict) -> object:
        query = 'SELECT * FROM users WHERE id=%(uid)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        user = cls(result[0])
        return user
    
    @classmethod
    def get_by_email(cls, data:dict) -> object:
        query = 'SELECT * FROM users WHERE email=%(email)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        user = cls(result[0])
        return user


    # static
    @staticmethod
    def create(data:dict) -> int:
        query = 'INSERT INTO users (name, email, pw) VALUES (%(name)s, %(email)s, %(pw)s);'
        id = connectToMySQL(DATABASE).query_db(query, data)
        return id
    
    @staticmethod
    def edit(data:dict) -> None:
        if len(data['pw']) != 0:
            query = 'UPDATE users SET name=%(name)s, pw=%(pw)s WHERE id=%(uid)s;'
        else:
            query = 'UPDATE users SET name=%(name)s WHERE id=%(uid)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def valid_signup(data:dict) -> bool:
        is_valid = True
        
        if User.get_by_email({'email': data['email']}):
            flash('Email already exists.', 'signup_email')
            is_valid = False

        if len(data['pw']) < 8:
            flash('Password need to be at least 8 characters.', 'signup_pw')
            is_valid = False
        
        if data['pw'] != data['confirm_pw']:
            flash("Passwords don't match.", 'signup_confirm_pw')
            is_valid = False
        
        return is_valid

    @staticmethod
    def valid_login(data:dict) -> bool:
        is_valid = True
        user = User.get_by_email({'email': data['email']})

        if not user:
            flash("Invlid email.", 'login_email')
            is_valid = False

        if is_valid:
            if not bcrypt.check_password_hash(user.pw, data['pw']):
                flash('Invalid password', 'login_pw')
                is_valid = False
        
        return is_valid

    @staticmethod
    def valid_edit(data:dict) -> bool:
        is_valid = True
        user = User.get_by_email({'email': data['email']})

        if len(data['pw']) < 8:
            flash('Password need to be at least 8 characters.', 'edit_pw')
            is_valid = False

        if data['pw'] != data['confirm_pw']:
            flash("Passwords don't match.", 'edit_confirm_pw')
            is_valid = False
        
        return is_valid