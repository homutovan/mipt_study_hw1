from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, TypeOfBusiness


class Controller:
    '''
    '''

    def __init__(self, DB_URI: str, VERBOSE: bool) -> None:
        self.engine = create_engine(DB_URI, echo=VERBOSE)

    
    def create_db(self) -> None:
        Base.metadata.create_all(self.engine)

    def destroy_db(self) -> None:
        Base.metadata.drop_all(self.engine)

        