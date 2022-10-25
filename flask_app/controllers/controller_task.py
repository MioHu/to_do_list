from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.model_task import Task
from flask_app.models.model_list import List

@app.route('/list/star_tasks')
def list_star_tasks():
    if 'uid' not in session:
        return redirect('/')
    all_lists = List.get_lists({'uid': session['uid']})
    star_tasks = Task.get_star_tasks({'uid': session['uid']})
    return render_template('star_tasks.html', all_lists=all_lists, star_tasks=star_tasks)

@app.route('/process_task_add/<int:lid>', methods=['POST'])
def process_task_add(lid):
    data = {
        'content': request.form['task_content'],
        'due_date': request.form['due_date'],
        'lid': lid
    }
    Task.add(data)
    return redirect(f'/list/{lid}')

@app.route('/task/delete/<int:lid>/<int:tid>')
def task_delete(lid, tid):
    Task.delete({'tid': tid})
    return redirect(f'/list/{lid}')

@app.route('/task/star/<int:lid>/<int:tid>')
def task_star(lid, tid):
    Task.star({'tid': tid})
    return redirect(f'/list/{lid}')

@app.route('/task/complete/<int:lid>/<int:tid>')
def task_complete(lid, tid):
    Task.complete({'tid': tid})
    return redirect(f'/list/{lid}')

@app.route('/list_task/delete/<int:id>')
def list_task_delete(id):
    List.delete({'uid': session['uid'], 'lid': id})
    all_list = List.get_lists({'uid': session['uid']})
    first_list = all_list[0]
    return redirect(f'/list/{first_list.id}')

@app.route('/list_task/star/<int:id>')
def list_task_star(id):
    List.star({'lid': id})
    return redirect(f'/list/{id}')

@app.route('/process_list_task_add', methods=['POST'])
def process_list_task_add():
    data = {
        'uid': session['uid'],
        'list_name': request.form['list_name']
    }
    id = List.add(data)
    return redirect(f'/list/{id}')

@app.route('/process_task_edit', methods=['POST'])
def process_task_edit():
    # don't know how to validate inside a dialog
    # use 'required', is it good enough?
    Task.edit(request.form)
    return redirect(f'/list/{request.form["lid"]}')
