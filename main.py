from db_controller import Controller
from settings import DB_URI, VERBOSE

if __name__ == '__main__':
    controller = Controller(DB_URI, VERBOSE)

    controller.create_db()