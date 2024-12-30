#!/usr/bin/python3
"""Script that prints State object with given name from database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        exit(1)

    # create connection
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, database)
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states with given name
    states = session.query(State).filter(State.name == sys.argv[4]).first()

    if states:
        print("{}".format(states.id))
    else:
        print("Not found")

    session.close()
