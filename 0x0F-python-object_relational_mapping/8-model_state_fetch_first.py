#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa """


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import Session
    from sqlalchemy import (create_engine)

    argv = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).first()
    if not state:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    session.close()
