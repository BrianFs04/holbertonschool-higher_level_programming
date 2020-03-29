#!/usr/bin/python3
'''
Script that lists all City objects from the database hbtn_0e_101_usa
'''
import sys
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    info = session.query(State, City).outerjoin(City).order_by(City.id)

    for state, city in info.all():
        print("{}: {} -> {}".format(city.id, city.name, state.name))
