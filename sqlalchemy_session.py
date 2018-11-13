from sqlalchemy import create_engine, Table, ForeignKey
from sqlalchemy import Column, Integer, String
from werkzeug.local import LocalProxy
from sqlalchemy.orm import scoped_session, relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'mysql+pymysql://root:@localhost:3306/bidongv2?charset=utf8')
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

some_sesion = Session()
other_session = Session()
another_session = Session()
print(some_sesion is other_session)
print(some_sesion is another_session)
proxy_session = LocalProxy(Session)


Base = declarative_base()

association = Table(
    "association", Base.metadata,
    Column("parent_id", Integer, ForeignKey('parent.id')),
    Column("child_id", Integer, ForeignKey('child.id'))
)

school = Table(
    "school", Base.metadata,
    Column("teacher_id", Integer, ForeignKey('teacher.id')),
    Column("child_id", Integer, ForeignKey('child.id'))
)


class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    children = relationship(
        "Child", secondary=school,
        back_populates="teachers", lazy="dynamic"
    )


class Parent(Base):
    __tablename__ = 'parent'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    children = relationship(
        "Child", secondary=association,
        back_populates="parents", lazy="dynamic"
    )

    @hybrid_property
    def children_count(self):
        return self.children.count()


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    parents = relationship(
        "Parent", secondary=association, back_populates="children")
    teachers = relationship(
        "Teacher", secondary=school, back_populates="children")

Base.metadata.create_all(bind=engine)

# father = Parent(name="LiLei")
# mother = Parent(name="HanMeimei")
# teacher = Teacher(name="Jim")
# proxy_session.add(father)
# proxy_session.add(mother)
# for n in range(20):
#     c = Child(name="LiXiaolei-{}".format(n))
#     proxy_session.add(c)
#     father.children.append(c)
#     mother.children.append(c)
#     if n < 10:
#         teacher.children.append(c)
# proxy_session.commit()

parent = proxy_session.query(Parent).all()[0]
print(parent.name)
print('hybrid_property: ', parent.children_count)
print(parent.children.count())

children = proxy_session.query(Child).all()
child = children[0]
print(child.name)
print(child.parents)
print(child.teachers)

child = children[-1]
print(child.teachers)
proxy_session.delete(child)
proxy_session.commit()

parent = proxy_session.query(Parent).all()[0]
print(parent.children.count())


# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(64))
#     password = Column(String(128))
# Base.metadata.create_all(bind=engine)
# user = User(name='wong', password='1234567')
# proxy_session.add(user)
# proxy_session.commit()
# rvs = proxy_session.query(User).all()
# print(rvs)
# proxy_session.close()
