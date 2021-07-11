from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField
from wtforms.fields.core import FormField, IntegerField
from wtforms.form import Form
from wtforms.validators import DataRequired, NumberRange, Email

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class EmailPasswordForm(FlaskForm):
    email   = StringField('Email', validators=[DataRequired(), Email()])
    password= PasswordField('password', validators=[DataRequired()])

class TelefonForm(FlaskForm):
    country_code    = IntegerField('Country Code', validators=[DataRequired()])
    area_code       = IntegerField('Area Code/Exhange', validators=[DataRequired()])
    number          = StringField('Number')

class ContactForm(FlaskForm):
    first_name  = StringField()
    last_name   = StringField()
    mobile_phone= FormField(TelefonForm) #TelephoneForm????
    office_phone= FormField(TelefonForm) #same as upper