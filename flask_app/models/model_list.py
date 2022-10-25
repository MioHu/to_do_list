from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.model_task import Task

class List:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.star = data['star']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.tasks = []
    

    # class
    @classmethod
    def get_lists(cls, data: dict) -> list:
        query = 'SELECT lists.id, lists.name, lists.star, lists.created_at, lists.updated_at FROM users, user_list AS ul, lists WHERE users.id=ul.user_id AND lists.id=ul.list_id AND users.id=%(uid)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return []
        lists = []
        for item in results:
            lists.append(cls(item))
        return lists
    
    @classmethod
    def list_with_tasks(cls, data:dict) -> object:
        if data['sort'] == 'due':
            query = 'SELECT * FROM lists, tasks WHERE lists.id=tasks.list_id AND lists.id=%(lid)s ORDER BY CASE WHEN due_date IS NULL THEN 1 ELSE 0 END;'
        elif data['sort'] == 'alpha':
            query = 'SELECT * FROM lists, tasks WHERE lists.id=tasks.list_id AND lists.id=%(lid)s ORDER BY content;'
        elif data['sort'] == 'create':
            query = 'SELECT * FROM lists, tasks WHERE lists.id=tasks.list_id AND lists.id=%(lid)s ORDER BY tasks.created_at;'
        else:
            query = 'SELECT * FROM lists, tasks WHERE lists.id=tasks.list_id AND lists.id=%(lid)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            query = 'SELECT * FROM lists WHERE id=%(lid)s;'
            result = connectToMySQL(DATABASE).query_db(query, data)
            return cls(result[0])
        list = cls(results[0])
        for row in results:
            task_data = {
                'id': row['tasks.id'],
                'content': row['content'],
                'due_date': row['due_date'],
                'complete': row['complete'],
                'star': row['tasks.star'],
                'created_at': row['tasks.created_at'],
                'updated_at': row['tasks.updated_at'],
                'list_id': row['list_id']
            }
            list.tasks.append(Task(task_data))
        return list

    
    # static
    @staticmethod
    def add(data:dict) -> int:
        query1 = 'INSERT INTO lists (name) VALUES (%(list_name)s);'
        lid = connectToMySQL(DATABASE).query_db(query1, data)
        query2 = f'INSERT INTO user_list VALUES ({data["uid"]}, {lid});'
        connectToMySQL(DATABASE).query_db(query2)
        return lid
    
    @staticmethod
    def delete(data:dict) -> None:
        query1 = 'DELETE FROM user_list WHERE user_id=%(uid)s AND list_id=%(lid)s;'
        connectToMySQL(DATABASE).query_db(query1, data)
        query2 = 'DELETE FROM lists WHERE id=%(lid)s;'
        connectToMySQL(DATABASE).query_db(query2, data)
        return
    
    @staticmethod
    def star(data:dict) -> None:
        query = 'UPDATE lists SET star=ABS(star-1) WHERE id=%(lid)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def edit(data:dict) -> None:
        query = 'UPDATE lists SET name=%(list_name)s WHERE id=%(lid)s;'
        return connectToMySQL(DATABASE).query_db(query, data)
    