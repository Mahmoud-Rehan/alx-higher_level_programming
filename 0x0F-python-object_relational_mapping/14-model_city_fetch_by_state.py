#!/usr/bin/python3
""" Script that lists all city objects from the database hbtn_0e_6_usa """
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:\
                            {argv[2]}@localhost:3306/{argv[3]}')
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City, State).join(State).all()

    for city, state in query:
        print(f"{state.name}: ({city.id}) {city.name}")
