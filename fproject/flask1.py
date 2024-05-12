from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('my.html')  # "<a href='/courses/1'>Courses</a>"

@app.get('/users')
def users_get():
    return 'GET /users'

@app.post('/users')
def users_post():
    return 'POST /users'

@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'
