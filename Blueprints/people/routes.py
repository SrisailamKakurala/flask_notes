from flask import request, render_template, redirect, url_for, Blueprint

from Blueprints.app import db
from Blueprints.people.models import Person

people = Blueprint('people', __name__, template_folder='templates')


@people.route('/')
def index():
    people = Person.query.all()
    return render_template('people/index.html', people=people)


@people.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('people/create.html')
    else:
        name = request.form['name']
        age = request.form['age']
        job = request.form['job']
        
        job = job if job != '' else None
        
        person = Person(name=name, age=age, job=job)
        db.session.add(person)
        db.session.commit()
        
        return redirect(url_for('people.index'))
        