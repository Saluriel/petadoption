from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message="Pet name cannot be blank")])
    species = SelectField("Species", choices=[('Dog', 'Dog'), ('Dat', 'Cat'), ('Porcupine', 'Porcupine')], validators=[InputRequired(message="Pet species cannot be blank")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30), Optional()])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes")
    available=BooleanField("Available for adoption")