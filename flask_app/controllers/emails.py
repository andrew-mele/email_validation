from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.email import Email


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create():
    if not Email.is_valid(request.form):
        return redirect('/')
    Email.create(request.form)
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html', emails=Email.get_all_emails())

@app.route('/delete/<int:id>')
def delete_email(id):
    data = {
        'id' : id
    }
    Email.delete(data)
    return redirect('/results')