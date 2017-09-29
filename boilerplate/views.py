from flask import render_template, redirect, request, flash
from . import app
from .database import db
from .forms import Contact
from .models import ContactForm

@app.route('/', methods=('GET', 'POST'))
def home():
    form = Contact()
    if request.method == 'POST':
        if form.validate_on_submit():
            contactForm = ContactForm(request.form['name'], request.form['emailid'], request.form['mobileno'])
            db.session.add(contactForm)
            db.session.commit()
            flash('Record was successfully added')
        return redirect('/')
    return render_template('index.html', form=form, contacts = ContactForm.query.all())
