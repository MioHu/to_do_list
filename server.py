from flask_app import app
from flask_app.controllers import controller, controller_user, controller_list, controller_task, controller_share

if __name__ == '__main__':
    app.run(debug=True)