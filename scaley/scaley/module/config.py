from db import *


def default_config_write():
    with configdb_connect as connection:
        c = connection.cursor()
        defaultcreds = [('AWSACCESSKEYID', 'NONE')
                        ('AWSACCESSSECRET', 'NONE')
                        ('RACKSPACEACCESSID', 'NONE')
                        ('RACKSPACESECRET', 'NONE')
                        ('OPENSTACKTOKENID', 'NONE')
                        ('OPENSTACKTOKEN', 'NONE')
                        ('AZUREACCESSID', 'NONE')
                        ('AZURESECRET', 'NONE')
                       ]
        c.executemany("INSERT INTO CLOUDCREDS VALUES (?, ?)", defaultcreds)

def update_config_write(value):
    with configdb_connect as connection:
        c = connection.cursor()
        c.executemany("INSERT INTO CLOUDCREDS VALUES (?, ?)", value)

def config_read(value):
    with configdb_connect as connection:
        c = connection.cursor()
        c.execute("SELECT * FROM CLOUDCREDS WHERE (?, ?)", value)
        rows = c.fetchall()
        return rows
