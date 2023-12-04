#!/usr/bin/python3
"""Start link class to table in database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, insert, update
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    """Base.metadata.create_all(engine)"""
    session = Session(engine)
    stmt = update(State).\
        values(name='New Mexico').\
        where(State.id == 2).\
    conn = engine.connect()
    state = conn.execute(stmt)

    session.close()
