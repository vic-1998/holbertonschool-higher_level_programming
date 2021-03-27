#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    db = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                   argv[2],
                                                                   argv[3]))
    Base.metadata.create_all(db)
    Session = sessionmaker(bind=db)
    session = Session()
    query = session.query(State).order_by(State.id).first()
    if query is not None:
        print("{}: {}".format(query.id, query.name))
    else:
        print("Nothing")
    session.close()
