#!/usr/bin/python3
"""
Python file similar to model_state.py named
model_city.py that contains the class definition of a City.
"""
from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    db = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                   argv[2],
                                                                   argv[3]))
    Base.metadata.create_all(db)
    Session = sessionmaker(bind=db)
    session = Session()
    query_row = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()
    for c, s in query_row:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
