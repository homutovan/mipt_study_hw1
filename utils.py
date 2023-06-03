from logging import StreamHandler, NullHandler, basicConfig, DEBUG, getLogger
from logging.handlers import RotatingFileHandler
import sys
import os

from settings import VERBOSE, log_file

if log_file:
    if not os.path.isdir('logs'):
        os.mkdir('logs')


def get_logger(name):
    '''
    '''

    stream_handler = StreamHandler(sys.stdout)
    file_handler = RotatingFileHandler(
        f'logs/{name}.log', 
        maxBytes=100000, 
        backupCount=100,
        ) or NullHandler()
    
    handlers = []

    if VERBOSE:
        handlers.append(stream_handler)

    if log_file:
        handlers.append(file_handler)

    basicConfig(
        handlers = handlers,
        format = '%(asctime)s %(levelname)-5s: %(processName) -25s: %(message)s',
        level = DEBUG,
    )

    logger = getLogger(name)
    logger.disabled = not (VERBOSE or log_file) 

    return logger