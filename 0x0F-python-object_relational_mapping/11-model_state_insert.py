#!/usr/bin/python3
"""Script to add State object 'Louisiana' to database"""

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
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, database)
    )

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # insert state
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)

    session.close()
