from flask import Flask, render_template, session, redirect, url_for, flash
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.fields import EmailField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Ishouldprobablyhaveabetterkey'
moment = Moment(app)
bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
 name = StringField('What is your name?', validators=[DataRequired()])
 email = EmailField('What is your UofT email address?', validators=[DataRequired(), Email()])
 submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        ## Flash messages
        old_name = session.get('name')
        old_email = session.get('email')
        if (old_name is not None and old_name != form.name.data):
            flash('Looks like you have changed your name!')
        if (old_email is not None and old_email != form.email.data):
            flash('Looks like you have changed your email!')
    
        ## Updating data
        session['name'] = form.name.data
        session['email'] = form.email.data
        form.email.data = ''
        form.name.data = ''

        ## Checking if email is a UofT email
        if ((session.get('email')).find('utoronto') == -1):
            session['email'] = 'non-uoft'

        return redirect(url_for('index'))

    return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, currentTime=datetime.utcnow())
