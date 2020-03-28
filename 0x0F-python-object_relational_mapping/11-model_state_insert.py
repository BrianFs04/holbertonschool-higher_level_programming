#!/usr/bin/python3
'''
Script that adds the State object “Louisiana” to the
database hbtn_0e_6_usa via SQLAlchemy
'''
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    newState = State(name='Louisiana')

    session.add(newState)
    session.commit()

    print(newState.id)
