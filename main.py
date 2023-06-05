from typing import Dict

from db.controller import Controller
from file_reader import FileReader
from settings import DB_URI, SOURCE1, SOURCE2, VERBOSE
from utils import get_logger
from validators import Company


class CustomReader(FileReader):
    @classmethod
    def parse_item(cls, item: Dict[str, str]) -> Dict[str, str] | None:
        okved = item.get(
            'data', {},
            ).get('СвОКВЭД', {}).get('СвОКВЭДОсн', {}).get('КодОКВЭД', '')

        if okved.split('.')[0] == '61':
            item['okved'] = okved
            return Company(**item).dict()


def init() -> Controller:
    controller = Controller(DB_URI, VERBOSE)
    controller.destroy_db()
    controller.create_db()
    return controller


def task_1(controller: Controller) -> None:
    controller.add_type_of_business(FileReader.read_json_by_path(SOURCE1))


def task_2(controller: Controller) -> None:
    for item in CustomReader.read_zip(SOURCE2):
        controller.add_company([item], commit=False)

    controller.commit()


if __name__ == '__main__':

    logger = get_logger(__name__)

    controller = init()
    task_1(controller)
    task_2(controller)
