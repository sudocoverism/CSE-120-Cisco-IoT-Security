#!/usr/bin/python
import sqlite3
from sqlite3 import Error



def main():
    database = r"data/tpch.sqlite"

    # create a database connection
    conn = connectToSQL(database)
    with conn:
        createDatabase(conn)
        fillDatabase(conn)
    closeConnection(conn, database)

def createDatabase(_conn):
    try:
        sql = """CREATE TABLE wgPeer(
    wg_publicKey varchar(255),
    wg_endPoint varchar(255),
    wg_allowedIPs varchar(255)
    );"""

        _conn.execute(sql)

        _conn.commit()


    except Error as e:
        print(e)
    

def fillDatabase(_conn):
    try:
        #peerInsert()
        sql = """INSERT INTO wgPeer
            VALUES('test', 'test', 'test')""" #% peerInsert)

        _conn.execute(sql)

        _conn.commit()


    except Error as e:
        print(e)

def connectToSQL(_dbFile):
    print(_dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
       
    except Error as e:
        print(e)

    return conn


def closeConnection(_conn, _dbFile):

    try:
        _conn.close()
    except Error as e:
        print(e)

if __name__ == '__main__':
    main()

