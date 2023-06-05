from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2
from models import Base, TypeOfBusiness, Company
from typing import List, Dict
from settings import THRESHOLD

from sqlalchemy.exc import SQLAlchemyError


class Driver:
    '''
    '''

    def __init__(self, DB_URI: str, VERBOSE: bool) -> None:
        self.engine = create_engine(DB_URI, echo=VERBOSE)
        self.session_factory = sessionmaker(self.engine, expire_on_commit=True)
        self._data_list = []

    
    def create_db(self) -> None:
        Base.metadata.create_all(self.engine)


    def destroy_db(self) -> None:
        Base.metadata.drop_all(self.engine)


    def add_data(self, data: List[Base], commit=True) -> bool:
        if commit:
            return self._add_record(data)
        
        else:
            self._data_list.append(*data)
            if len(self._data_list) >= THRESHOLD:
                return self.commit()
            return True


    def _add_record(self, data: List[Base]) -> bool:
        try:
            with self.session_factory() as session:
                session.add_all(data)
                session.commit()

            return True
        
        except SQLAlchemyError as e:
            print(e)
            return False
        
        
    def commit(self) -> bool:
        data = [*self._data_list]
        self._data_list = []
        return self._add_record(data)
    

class Controller(Driver):
    '''
    '''

    def add_type_of_business(self, data: List[Dict[str, str]], commit=True) -> bool:
        return self.add_data(list(map(
            lambda x: TypeOfBusiness(**x), data)), commit=commit
            )
    
    def add_company(self, data: List[Dict[str, str]], commit=True) -> bool:
        return self.add_data(list(map(
            lambda x: Company(**x), data)), commit=commit
            )
    
