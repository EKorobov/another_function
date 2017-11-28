#!/usr/bin/env python

import os
import json
import logging
import time

STORAGE_ACCOUNT_NAME = 'anotherfunction'
STORAGE_ACCOUNT_KEY = 'vpOLqCeARq7wL0YlIC45/HprNzGzTVDAYwcn8FqSES8dVXYtO89cGsyN4Fx7eLtLY/U/+jcMyJzs3lt3KqyCUQ=='

started_at = int(time.time())

class FromStartFilter(logging.Filter):
    def __init__(self, start_time):
        self.start_time = start_time

    def filter(self, record):
        record.from_start = time.time() - self.start_time
        return True

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

_sh = logging.StreamHandler()
_fmt = logging.Formatter(fmt='[%(from_start)3ss] %(message)s')
_filter = FromStartFilter(start_time=started_at)

_sh.setLevel(logging.INFO)
_sh.setFormatter(_fmt)
_sh.addFilter(_filter)

logger.addHandler(_sh)
logger.info('finished logging initialization')


logger.info('before opening res file')
with open(os.environ['res'], 'w') as res:
    logger.info('opened res file')
    try:
        logger.info('trying to import azure.storage.table.TableService')
        from azure.storage.table import TableService
        logger.info('imported azure.storage.table.TableService')

        logger.info('trying to import azure.storage.table.Entity')
        from azure.storage.table import Entity
        logger.info('imported azure.storage.table.Entity')
    except ImportError as ex:
        logger.info('ImportError: %s', ex)

        logger.info('before res.write (about error)')
        res.write('import error')
        logger.info('after res.write (about error)')
    else:
        logger.info('no import errors, we are in `else` block')

        logger.info('before res.write (about successful import)')
        res.write('successfully imported from azure.storage.table')
        logger.info('after res.write (about successful import)')
logger.info('after closing res file')

logger.info('before opening req file')
with open(os.environ['req'], 'r') as fp:
    logger.info('opened req file')
    try:
        logger.info('trying to json.load(fp)')
        print(json.load(fp))
        logger.info('successfully loaded json from req file')
    except json.JSONDecodeError as ex:
        logger.info('JSONDecodeError: %s', ex)

        logger.info('going to fp.read() and print it')
        print(fp.read())
        logger.info('printing fp.read() done')
logger.info('after closing req file')


