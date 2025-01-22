from app import app
from models import db, Message

with app.app_context():
    db.create_all()
    sample_message = Message(body="Hello, World!", username="Admin")
    db.session.add(sample_message)
    db.session.commit()
