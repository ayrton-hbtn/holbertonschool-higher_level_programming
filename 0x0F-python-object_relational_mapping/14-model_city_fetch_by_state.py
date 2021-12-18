#!/usr/bin/python3
"""  prints all City objects from the database hbtn_0e_14_usa """


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, asc

    argv = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    sc = session.query(State, City).filter(State.id == City.state_id)\
                .order_by(asc(City.id)).all()
    for i in sc:
        print("{}: ({}) {}".format(i.State.name, i.City.id, i.City.name))
    session.close()
