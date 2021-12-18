#!/usr/bin/python3
""" adds the State object “Louisiana” to the database hbtn_0e_6_usa """


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import Session
    from sqlalchemy import insert
    from sqlalchemy import (create_engine)

    argv = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    newState = State(name='Louisiana')
    session.add(newState)
    session.commit()
    print(newState.id)
    session.close()
