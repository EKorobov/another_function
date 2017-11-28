#!/usr/bin/env python

import os
import json

with open(os.environ['res'], 'w') as res:
    try:
        from azure.storage.table import TableService, Entity
    except ImportError as ex:
        res.write('import error')
    else:
        res.write('successfully imported from azure.storage.table')
    
with open(os.environ['req'], 'r') as fp:
    try:
        print(json.load(fp))
    except json.JSONDecodeError as ex:
        print(fp.read())

