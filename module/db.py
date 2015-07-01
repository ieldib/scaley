import sqlite3

##create a new db if it doesn't exist



def configdb_connect(section, field, values):
    return sqlite3.connect('../db/config.db')
