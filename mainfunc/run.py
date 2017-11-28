#!/usr/bin/env python

import os, sys, platform

with open(os.environ['req'], 'r') as inp:
    print(inp)

with open(os.environ['res'], 'w') as res:
    res.write(platform.python_version)

