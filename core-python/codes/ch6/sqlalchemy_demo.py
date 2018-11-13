import os
import random


from sqlalchemy import Column, Integer, String, create_engine, exc, orm
from sqlalchemy.ext.declarative import declarative_base

COLSIZE = 10
DB_NAME = 'core_python_users'
DB_USER = 'root'
DB_HOST = 'localhost'
DB_PORT = 3306
DB_PASSWORD = ''
DSN = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db}'.format(
    user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT, db=DB_NAME)

NAMES = [
    ('arron', 8312), ('angela', 7603), ('dave', 7306), ('davina', 7902),
    ('elliot', 7911), ('wong', 6689), ('xin', 7312), ('jie', 6379)
]


def get_names():
    pick = set(NAMES)
    while pick:
        yield pick.pop()


Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    login = Column(String(32))
    project_id = Column(Integer)

    def __str__(self):
        return ','.join(map(str, (self.user_id, self.login, self.project_id)))


class SQLAlchemyTest(object):

    def __init__(self, dsn):
        try:
            engine = create_engine(dsn, echo=True)
        except ImportError as err:
            raise RuntimeError()
        try:
            engine.connect()
        except (exc.OperationalError, exc.InternalError) as err:
            engine = create_engine(os.path.dirname(dsn), echo=True)
            engine.execute("CREATE DATABASE `%s` DEFAULT CHARSET=utf8" % DB_NAME).close()
            engine = create_engine(dsn, echo=True)

        Session = orm.sessionmaker(bind=engine)
        self.session = Session()
        self.users = Users.__table__
        self.engine = self.users.metadata.bind = engine

    def insert(self):
        self.session.add_all(
            Users(login=who, user_id=user_id, project_id=random.randrange(1, 5))
            for who, user_id in get_names()
        )
        self.session.commit()

    def update(self):
        fr = random.randrange(1, 5)
        to = random.randrange(1, 5)

        users = self.session.query(Users).filter_by(project_id=fr).all()
        for user in users:
            user.project_id = to
        self.session.commit()

        return fr, to, len(users)

    def delete(self):
        rm = random.randrange(1, 5)

        users = self.session.query(Users).filter_by(project_id=rm).all()
        for user in users:
            self.session.delete(user)
        self.session.commit()
        return rm, len(users)

    def db_dump(self):
        print("user_id,login,project_id")
        users = self.session.query(Users).all()
        for user in users:
            print(user)
        self.session.commit()

    def __getattr__(self, attr):
        return getattr(self.users, attr)

    def finish(self):
        return self.session.connection().close()


def main():
    print("*** Connect to %r database" % DB_NAME)

    orm = SQLAlchemyTest(DSN)

    print("*** Create users table")
    orm.drop(checkfirst=True)
    orm.create()

    print("*** Insert names into table")
    orm.insert()
    orm.db_dump()

    print("*** Move users to random group")
    fr, to, num = orm.update()
    orm.db_dump()

    print("** Randomly delete group")
    rm, num = orm.delete()
    orm.db_dump()

    print("*** Drop users table")
    orm.drop()
    orm.finish()


if __name__ == "__main__":
    main()
