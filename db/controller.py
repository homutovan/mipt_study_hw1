from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from psycopg2 import errors
from models import Base, TypeOfBusiness
from typing import List, Dict


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
            return True


    def _add_record(self, data: List[Base]) -> bool:
        try:
            with self.session_factory() as session:
                session.add_all(data)
                session.commit()

            return True
        
        except errors.StringDataRightTruncation:
            print('value too long for type character')
        
        except Exception as e:
            print(e)##################################
            print('ERROR!!')##########################
            raise Exception(e)
            return False
        

    def commit(self) -> bool:
        data = [*self._data_list]
        self._data_list = []
        return self._add_record(data)
    

class Controller(Driver):
    '''
    '''

    def add_type_of_business(self, data: List[Dict[str, str]]) -> bool:
        return self.add_data(list(map(
            lambda x: TypeOfBusiness(**x), data))
            )
    
    