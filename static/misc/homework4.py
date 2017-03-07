#!/usr/bin/env python
'''Ingest the CMOA catalogue and build database'''

# import statements
import json
import sys
import sqlite3

# global values
FILE_JSON = "catalog.json"
FILE_DB = "cmoa.db"

# class definitions
class CMOAdb(object):
    '''A connection to the CMOA db'''
    
    valid_fields = [
        'id', 
        'title',
        'creator',
        'medium',
        'nationality',
        'date'
    ]
    
    def __init__(self, file_db, file_json):
        '''Create a new connection'''
        
        self.file = file_db
        self.conn =                     # TODO create a connection
        self.conn.row_factory = sqlite3.Row
    
        self._create_tables()
        self._populate_tables(file_json)

    
    def _create_tables(self):
        '''Create necessary tables'''
        
        cur =                           # TODO create cursor
        
        # get rid of any existing data
        cur.execute()                   # TODO if table exists, drop it
        
        # create the new table
        create_sql =                    # TODO sql to create the table

                                        # TODO use cursor to execute sql

        
    def _populate_tables(self, file):
        '''Fill the table using data from json file'''
        
        with open(file) as fh:
            data = json.load(fh)
        
        cur =                           # TODO create cursor
        
        row_sql =                       # TODO sql insert statement to add row
            
                                        # TODO use cursor to execute sql
                                        
                                        # TODO use connection to commit changes


    def get_artthings(self, field, value):
        '''Search for rows that match a set of criteria'''
        
        result = []
        
        if field in CMOAdb.valid_fields:
            cur =                       # TODO create cursor
            
            query_sql =                 # TODO sql query statement
            
                                        # TODO use cursor to execute sql

            result =                    # TODO use cursor to get all results
        
        return result


# main block

if __name__ == '__main__':
    db = CMOAdb(FILE_DB, FILE_JSON)
    
    field = sys.argv[1]
    value = sys.argv[2]
    
    for row in db.get_artthings(field, value):
        print u'{} ({}) "{}"'.format(row['creator'], row['date'], row['title'])
