#!/usr/bin/python3
"""
Script that deletes all State objects witha name
containing the letter a from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
import sqlalchemy
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                   argv[2],
                                                                   argv[3]))
    Base.metadata.create_all(db)
    Session = sessionmaker(bind=db)
    session = Session()
    query_rows = session.query(State).filter(State.name.like('%a%'))
    for x in query_rows:
        session.delete(x)
    session.commit()
    session.close()
