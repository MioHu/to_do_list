from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.model_list import List

@app.route('/dashboard')
def dashboard():
    if 'uid' not in session:
        return redirect('/')
    lists = List.get_lists({'uid': session['uid']})
    return render_template('dashboard.html', lists=lists)

@app.route('/process_list_add', methods=['POST'])
def process_list_add():
    data = {
        'uid': session['uid'],
        'list_name': request.form['list_name']
    }
    List.add(data)
    return redirect('/dashboard')

@app.route('/list/<int:id>')
def list_one(id):
    if 'uid' not in session:
        return redirect('/')
    all_lists = List.get_lists({'uid': session['uid']})
    list = List.list_with_tasks({'lid': id, 'sort': ''})
    return render_template('list.html', all_lists=all_lists, list=list)

# these three routes are used to sort
# I don't think it's a good idea, but how can I sort in only one route
@app.route('/list/due/<int:id>')
def list_due(id):
    if 'uid' not in session:
        return redirect('/')
    all_lists = List.get_lists({'uid': session['uid']})
    list = List.list_with_tasks({'lid': id, 'sort': 'due'})
    return render_template('list.html', all_lists=all_lists, list=list)

@app.route('/list/alpha/<int:id>')
def list_alpha(id):
    if 'uid' not in session:
        return redirect('/')
    all_lists = List.get_lists({'uid': session['uid']})
    list = List.list_with_tasks({'lid': id, 'sort': 'alpha'})
    return render_template('list.html', all_lists=all_lists, list=list)

@app.route('/list/create/<int:id>')
def list_create(id):
    if 'uid' not in session:
        return redirect('/')
    all_lists = List.get_lists({'uid': session['uid']})
    list = List.list_with_tasks({'lid': id, 'sort': 'create'})
    return render_template('list.html', all_lists=all_lists, list=list)

@app.route('/list/delete/<int:id>')
def list_delete(id):
    List.delete({'uid': session['uid'], 'lid': id})
    return redirect('/dashboard')

@app.route('/list/star/<int:id>')
def list_star(id):
    List.star({'lid': id})
    return redirect('/dashboard')

@app.route('/process_list_edit', methods=['POST'])
def process_list_edit():
    # don't know how to validate inside a dialog
    List.edit(request.form)
    return redirect(f'/list/{request.form["lid"]}')