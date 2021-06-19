from flask import Blueprint, render_template, request
from foodtracker.models import Food
from foodtracker.extensions import db


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add')
def add():
    return render_template('add.html')

@main.route('/add', methods=['POST'])
def add_post():
    food_name = request.form.get('food-name')
    proteins = request.form.get('protein')
    fats = request.form.get('fat')
    carbs = request.form.get('carbohydrates')

    #code here basically contols all the functionality of the add feature

    new_food = Food(name = food_name, 
        proteins = proteins, 
        carbs =carbs, 
        fats=fats)

    db.session.add(new_food)
    db.session.commit()

    return f'<h1>{ food_name } - { proteins} - { carbs } - { fats }<h1/>'

    


@main.route('/view')
def view():
    return render_template('view.html')