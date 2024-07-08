#!/usr/bin/python3
""" script that creates
    the State California with
    the City San Francisco from the databas """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb\
            ://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    session.add(new_state)
    session.commit()
    session.close()
