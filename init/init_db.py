"""
    File Name: init_db.py
    Create On 2017/03/22
    Description: This script is used to init database, liking:
                creating table according to your models. Before
                you execute this script, the database should to
                be created first.
"""

import sys
sys.path.append("..")
from models.model import db


def _init_database(db):
    print "Begin to create tables accroding to models..."
    try:
        db.create_all()
        print "The tables had been created..." 
    except Exception as e:
        print "Create tables error: {0}".format(e)
        

if __name__ == "__main__":
    _init_database(db)
    sys.exit(0)