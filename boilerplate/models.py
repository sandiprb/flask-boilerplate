from .database import db

class ContactForm(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    emailid = db.Column(db.String(128))
    mobileno = db.Column(db.String(13))

    def __init__(self, name, emailid, mobileno):
        self.name = name
        self.emailid = emailid
        self.mobileno = mobileno
