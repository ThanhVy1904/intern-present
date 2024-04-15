from app import app
from flask import render_template, flash, redirect
from app.forms import ContactForm

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    sentMessage = None
    if form.validate_on_submit():
        sentMessage = 'Sent'
    return render_template('index.html', title='Home', form=form, sentMessage=sentMessage)

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html', title='About Me')

@app.route('/experience')
def experience():
    return render_template('experience.html', title='Experience')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    sentMessage = None
    if form.validate_on_submit():
        sentMessage = 'Sent'
    return render_template('contact.html', title='Contact', form=form, sentMessage=sentMessage)
