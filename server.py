from flask import Flask, redirect, render_template, session, request, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "WowMuchSeckrets"

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if(len(request.form['email']) < 1):
        flash("Name cannot be empty!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address")
    else:
        flash("Success!")
    return redirect('/')

app.run(debug=True)