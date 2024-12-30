#!/usr/bin/python3
"""Script to change name of State object in database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        exit(1)

    # create connection
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}@localhost:3306/{}".format(username, password, database)
    )

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states to change name
    states = session.query(State).filter(State.id == 2).first()

    if states:
        states.name = "New Mexico"
        session.commit()

    session.close()
