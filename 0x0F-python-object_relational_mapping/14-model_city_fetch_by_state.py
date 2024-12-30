#!/usr/bin/python3
"""Script to print all City objects from database"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import Create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'. format(sys.argv[1]), sys.argv[2], sys.argv[3])

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).filter(State.id == City.state_id)\.order_by(City.id).all()

    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    
    session.close()
