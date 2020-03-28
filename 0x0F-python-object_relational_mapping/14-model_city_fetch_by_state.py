#!/usr/bin/python3
'''
Script that prints all City objects from
the database hbtn_0e_14_usa via SQLAlchemy
'''
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    info = session.query(State, City).filter(State.id == City.state_id)
    for state, city in info.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
