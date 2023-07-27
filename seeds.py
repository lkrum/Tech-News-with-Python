from app.models import User
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert users
db.add_all([
  User(username='naruto', email='narutobelieveit@yahoo.com', password='password123'),
  User(username='sasukeuchiha', email='thelastuchiha@gmail.com', password='password123'),
  User(username='sharuno', email='sakuraharuno@gmail.com', password='password123'),
  User(username='khatake', email='kakashi8@gmail.com', password='password123'),
  User(username='itachiUchiha', email='itachi@hotmail.com', password='password123')
])

db.commit()

db.close()