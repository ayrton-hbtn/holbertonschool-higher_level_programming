#!/usr/bin/python3
"""  lists all State objects that contain the letter a """


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
    states = session.query(State).order_by(State.id)\
                    .filter(State.name.like('%a%')).all()
    for st in states:
        print("{}: {}".format(st.id, st.name))
    session.close()
