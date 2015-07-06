import sqlite3

def configdb_connect(section, field, values):
    return sqlite3.connect('../db/config.db')
