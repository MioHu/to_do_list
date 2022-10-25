from flask import render_template, request, redirect, session
from flask_app import app, bcrypt
from flask_app.models.model_user import User
from flask_app.models.model_list import List

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/process_signup', methods=['POST'])
def process_signup():
    #validate
    if not User.valid_signup(request.form):
        return redirect('/signup')
    #hash
    pw_hash = bcrypt.generate_password_hash(request.form['pw'])
    data = {
        **request.form,
        'pw': pw_hash
    }
    #create
    session['uid'] = User.create(data)
    return redirect('/dashboard')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/process_login', methods=['POST'])
def process_login():
    #validate
    if not User.valid_login(request.form):
        return redirect('/login')
    #save in session for later use
    user = User.get_by_email({'email': request.form['email']})
    session['uid'] = user.id
    return redirect('/dashboard')

@app.route('/user')
def user():
    if 'uid' not in session:
        return redirect('/')
    all_lists = List.get_lists({'uid': session['uid']})
    user = User.get_one({'uid': session['uid']})
    return render_template('user.html', all_lists=all_lists , user=user)

@app.route('/process_user_edit', methods=['POST'])
def process_user_edit():
    if len(request.form['pw']) == 0:
        User.edit(request.form)
    else:
        if not User.valid_edit(request.form):
            return redirect('/user')
        data = {
            **request.form,
            'pw': bcrypt.generate_password_hash(request.form['pw'])
        }
        User.edit(data)
    return redirect('/user')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')