from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, TextField, SelectField
from wtforms.validators import InputRequired

choices = [('house','House'), ('apartment','Apartment')]
class PropertyForm(FlaskForm):
    title = TextField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    bedrooms = TextField('No. of Bedrooms', validators=[InputRequired()])
    bathrooms = TextField('No. of Bathrooms', validators=[InputRequired()])
    location = TextField('Location', validators=[InputRequired()])
    price = TextField('Price', validators=[InputRequired()])
    proptype = SelectField(u'Property Type', choices =choices)
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png'], 'Photos only!')])