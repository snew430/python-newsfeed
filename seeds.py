from app.models import User
from app.db import Session, Base, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

db.add_all([
    User(username='bob', email='bob@bob.com', password='pass1234'),
    User(username='sally', email='sally@sally.com', password='pass1234'),
    User(username='jimbo', email='jimbo@jimbo.com', password='pass1234'),
    User(username='sean', email='sean@sean.com', password='pass1234'),
    User(username='kerry', email='kerry@kerry.com', password='pass1234')
    ])

db.commit()

db.close()