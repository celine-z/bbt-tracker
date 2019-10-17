from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from .models import Store


class StoreForm(FlaskForm):
    name = StringField('Name of Store', validators=[DataRequired(), Length(max=20)])
    comments = TextAreaField(validators=[Length(max=250)])
    submit = SubmitField('submit')

    def validate_name(self, field):
        if Store.query.filter_by(name=field.data).first():
            raise ValidationError("Store already exists")


class DrinkForm(FlaskForm):
    name = StringField('Name of Drink', validators=[DataRequired(), Length(max=50)])
    sugar_level = IntegerField('Sugar Level (%)', validators=[NumberRange(min=0, max=100)])
    ice_level = IntegerField('Ice Level (%)', validators=[NumberRange(min=0, max=100)])
    rating = IntegerField('Rating (/10)', validators=[NumberRange(min=0, max=10)])
    comments = TextAreaField(Length(max=250))
    submit = SubmitField('submit')
