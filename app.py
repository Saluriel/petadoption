from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def homepage_list_pets():
    """Homepage where you view a list of pets for adoption"""

    pets = Pet.query.all()
    

    return render_template('list_pets.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet_form():
    """Renders the pet form (GET) or handles the snack form (POST)"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url=form.photo_url.data
        age=form.age.data
        notes=form.notes.data
        
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/<pet_id>', methods=["GET", "POST"])
def display_and_edit_pet(pet_id):
    """Displays information about a pet and handles the edit form (POST)"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()

    if form.validate_on_submit():
        pet.photo_url=form.photo_url.data
        pet.notes=form.notes.data
        pet.available=form.available.data
        db.session.commit()
        return redirect(f'/{pet_id}')
    else:
        return render_template('display_edit_pet.html', form=form, pet=pet)