from flask import Flask, render_template, request, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = 'secret_key'

users = ['mike', 'mishel', 'adel', 'keks', 'kamila']

@app.route('/')
def hello():
    return render_template('my.html')  # "<a href='/courses/1'>Courses</a>"

@app.get('/users')
def users_get(): 
    term = request.args.get('term', '')
    if term:
        filtered = [user for user in users if (term in user)]
        flash(f'Filtered: "{term}"', 'success')
    else:
        filtered = users
    msg = get_flashed_messages(with_categories=True)
    return render_template('/users/index.html', users=filtered, search=term, messages=msg)

@app.post('/users')
def users_post():
    return 'POST /users'

@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'
