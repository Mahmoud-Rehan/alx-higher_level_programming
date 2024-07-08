#!/usr/bin/python3
""" script that lists all State objects,
    and corresponding City objects,
    contained in the database """
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__== "__main__":
    engine = create_engine("mysql+mysqldb://{argv[1]}:{argv[2]}\
            @localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
