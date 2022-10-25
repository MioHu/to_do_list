from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Task:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.content = data['content']
        self.due_date = data['due_date']
        self.complete = data['complete']
        self.star = data['star']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.list_id = data['list_id']
    

    @classmethod
    def get_one(cls, data:dict) -> object:
        query = 'SELECT * FROM tasks WHERE id=%(tid)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        task = cls(result[0])
        return task

    @staticmethod
    def add(data:dict) -> int:
        if len(data['due_date']) == 0:
            query = 'INSERT INTO tasks (content, list_id) VALUES (%(content)s, %(lid)s);'
        else:
            query = 'INSERT INTO tasks (content, due_date, list_id) VALUES (%(content)s, %(due_date)s, %(lid)s);'
        id = connectToMySQL(DATABASE).query_db(query, data)
        return id
    
    @staticmethod
    def delete(data:dict) -> None:
        query = 'DELETE FROM tasks WHERE id=%(tid)s;'
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @staticmethod
    def star(data:dict) -> None:
        query = 'UPDATE tasks SET star=ABS(star-1) WHERE id=%(tid)s;'
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @staticmethod
    def complete(data:dict) -> None:
        query = 'UPDATE tasks SET complete=ABS(complete-1) WHERE id=%(tid)s;'
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @staticmethod
    def get_star_tasks(data:dict) -> list:
        query = 'SELECT * FROM users, user_list, tasks WHERE users.id=user_list.user_id AND user_list.list_id=tasks.list_id AND users.id=%(uid)s AND tasks.star=1;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return []
        star_tasks = []
        for row in results:
            task_data = {
                'id': row['tasks.id'],
                'content': row['content'],
                'due_date': row['due_date'],
                'complete': row['complete'],
                'star': 1,
                'created_at': row['tasks.created_at'],
                'updated_at': row['tasks.updated_at'],
                'list_id': row['tasks.list_id']
            }
            star_tasks.append(Task(task_data))
        return star_tasks
    
    @staticmethod
    def edit(data:dict) -> None:
        if len(data['due_date']) == 0:
            query = 'UPDATE tasks SET content=%(task_content)s, due_date=NULL, list_id=%(lid)s WHERE id=%(tid)s;'
        else:
            query = 'UPDATE tasks SET content=%(task_content)s, due_date=%(due_date)s, list_id=%(lid)s WHERE id=%(tid)s;'
        return connectToMySQL(DATABASE).query_db(query, data)