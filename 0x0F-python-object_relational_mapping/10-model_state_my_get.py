#!/usr/bin/python3
""" prints the State object with the name passed as argument """


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
    state = session.query(State).filter(State.name.like(argv[4])).all()
    if not state:
        print("Not found")
    else:
        print(state[0].id)
    session.close()
