#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/item_catalog/")

from __init__ import app as application
application.secret_key = 'my project item catalog secret'