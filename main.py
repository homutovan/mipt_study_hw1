from db.controller import Controller
from settings import DB_URI, VERBOSE, SOURCE1
from file_reader import filereader

from models import TypeOfBusiness

if __name__ == '__main__':

    controller = Controller(DB_URI, VERBOSE)
    controller.destroy_db()
    controller.create_db()
    controller.add_type_of_business(filereader(SOURCE1))

