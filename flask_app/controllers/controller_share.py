from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.model_share import Share
from flask_app.models.model_user import User
from flask_app.models.model_list import List

@app.route('/process_list_share/<int:lid>', methods=['POST'])
def process_list_share(lid):
    user = User.get_by_email({'email': request.form['to_email']})
    if not user:
        flash("We don't have this user.", 'send')
        return redirect(f'/list/{lid}/back')
    data = {
        'from_id': session['uid'],
        'to_id': user.id,
        'list_id': lid
    }
    if not Share.send_validate(data):
        return redirect(f'/list/{lid}/back')
    Share.send(data)
    return redirect(f'/list/{lid}')


# Problem: if send invalid, I want to keep the collapse and show flash message
# it's not the best way to solve the problem, but I don't have time
@app.route('/list/<int:id>/back')
def list_back(id):
    if 'uid' not in session:
        return redirect('/')
    all_lists = List.get_lists({'uid': session['uid']})
    list = List.list_with_tasks({'lid': id, 'sort': ''})
    return render_template('list_back.html', all_lists=all_lists, list=list)

@app.route('/message')
def message():
    if 'uid' not in session:
        return redirect('/')
    all_lists = List.get_lists({'uid': session['uid']})
    share_from_me = Share.get_from({'uid': session['uid']})
    share_to_me = Share.get_to({'uid': session['uid']})
    return render_template('message.html', all_lists=all_lists, share_from_me=share_from_me, share_to_me=share_to_me)

@app.route('/process_share', methods=['POST'])
def process_share():
    if request.form['accept'] == 'accept':
        Share.receive_accept(request.form)
    else:
        Share.receive_reject(request.form)
    return redirect('/message')