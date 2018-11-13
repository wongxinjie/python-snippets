from sqlalchemy import event
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from werkzeug.local import LocalProxy
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect

engine = create_engine(
    'mysql+pymysql://root:@localhost:3306/bidong?charset=utf8')
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
proxy_session = LocalProxy(Session)

Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)
    mobile = Column(String(32))

Base.metadata.create_all(bind=engine)

teachers = [
    {"name": "Lily", "age": 24, "mobile": 1},
    {"name": "Lucy", "age": 27, "mobile": 2}
]

for kw in teachers:
    model = Teacher(**kw)
    proxy_session.add(model)
proxy_session.commit()


@event.listens_for(Teacher, "after_update")
def teacher_modify(mapper, connection, target):
    state = inspect(target)
    chanages = {}
    for attr in state.attrs:
        print(attr.key)
        hist = state.get_history(attr.key, True)

        print(hist.has_changes())
        if not hist.has_changes():
            continue

        print(dir(hist))
        chanages[attr.key] = hist.added

    print(chanages)
    print(target.id, target.name, target.age, target.mobile)


@event.listens_for(Teacher, "after_bulk_delete")
def teacher_remove(mapper, connection, target):
    print(target.id, target.name, target.age, target.mobile)

# teacher = proxy_session.query(Teacher).all()[0]
proxy_session.query(Teacher).filter_by(name="Lucy").delete()
proxy_session.commit()
