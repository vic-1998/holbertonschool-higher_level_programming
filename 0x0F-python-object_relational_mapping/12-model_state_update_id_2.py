#!/usr/bin/python3
"""
Script that changes the name of a State object
from the database hbtn_0e_6_usa
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
    query_rows = session.query(State).filter_by(id=2).first()
    query_rows.name = "New Mexico"
    session.commit()
    session.close()
