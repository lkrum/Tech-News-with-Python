from app.models import User, Post, Comment, Vote
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

# insert posts
db.add_all([
  Post(title='Donec posuere metus vitae ipsum', post_url='https://buzzfeed.com/in/imperdiet/et/commodo/vulputate.png', user_id=1),
  Post(title='Morbi non quam nec dui luctus rutrum', post_url='https://nasa.gov/donec.json', user_id=1),
  Post(title='Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue', post_url='https://europa.eu/parturient/montes/nascetur/ridiculus/mus/etiam/vel.aspx', user_id=2),
  Post(title='Nunc purus', post_url='http://desdev.cn/enim/blandit/mi.jpg', user_id=3),
  Post(title='Pellentesque eget nunc', post_url='http://google.ca/nam/nulla/integer.aspx', user_id=4)
])

db.commit()

# insert comments
db.add_all([
  Comment(comment_text='Great job', user_id=3, post_id=2),
  Comment(comment_text='ehh it was ok.', user_id=1, post_id=3),
  Comment(comment_text='AMAZING', user_id=3, post_id=1),
  Comment(comment_text='Insightful details. Never would have considered this', user_id=2, post_id=3),
  Comment(comment_text='I liked it.', user_id=3, post_id=3)
])

db.commit()

# insert votes
db.add_all([
  Vote(user_id=1, post_id=2),
  Vote(user_id=5, post_id=4),
  Vote(user_id=2, post_id=4),
  Vote(user_id=3, post_id=4),
  Vote(user_id=4, post_id=2)
])

db.commit()

db.close()