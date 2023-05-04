from wtforms import Form, StringField, PasswordField, validators

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=50)])
    password = PasswordField('Password', [validators.DataRequired()])
