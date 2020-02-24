from flask import Flask, render_template, request, redirect, url_for
from model import add_user

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        password_check = request.form['password_check']
        add_user(name, email, password)
        return redirect('/users/' + name)
    return render_template('index.html')

@app.route('/users/<name>')
def user_page(name):
    return render_template('user.html', name=name)


app.run(debug=True) # app.run('0.0.0.0', '3000', debug=True)
