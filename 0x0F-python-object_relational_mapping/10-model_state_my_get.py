#!/usr/bin/python3
"""
prints the State object with the name passed as argument from
the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create the engine and bind the metadata to it.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Base.metadata.create_all(engine)

    # Create a session to interact with the database.
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with the specified name
    state = session.query(State).filter(State.name == (state_name,)).first()

    # Print the result
    if state is not None:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
