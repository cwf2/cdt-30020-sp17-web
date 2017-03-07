#!/usr/bin/env python
'''Interact with a catalogue of children's fiction'''

# import statements
import sqlite3
import sys
import os

# global values
DB_FILE = 'kidslit.db'
AUTH_FILE = 'authors.tsv'
BOOK_FILE = 'books.tsv'

# class definitions
class LibraryDB(object):
    '''A connection to the library database'''
    
    def __init__(self, db_file, auth_file, book_file):
        '''Initialize a new conenction to the database'''
        
        # save initialization variables
        self.db_file = db_file
        self.auth_file = auth_file
        self.book_file = book_file
        
        # open connection to database
        self.conn = sqlite3.connect(db_file)
        
        # allow column access by name
        #self.conn.row_factory = sqlite3.Row
        
        # enforce foreign key constraints
        self.conn.execute('PRAGMA foreign_keys = ON')
        
        # initialize the tables
        self._build_tables()
        self._populate_tables()
        
    
    def _build_tables(self, clobber=True):
        '''Initialize the database tables'''
        
        # new cursor
        cur = self.conn.cursor()
        
        # delete existing tables?
        if clobber:
            cur.execute('''
            DROP TABLE IF EXISTS Book
            ''')
            cur.execute('''
            DROP TABLE IF EXISTS Author
            ''')

        
        # create tables
        cur.execute()        # TODO fill in some SQL for Author table

        cur.execute()        # TODO fill in some SQL for Book table

        
    def _populate_tables(self):
        '''Fill the tables using TSV data'''
        
        # new cursor
        cur = self.conn.cursor()
        
        # populate Author
        with open(self.auth_file) as fh:
            # discard header
            fh.readline()
            
            insert_sql = ''  # TODO add some SQL here for the Author INSERT
            
            for line in fh:
                rec = line.split('\t')
                if len(rec) == 6:
                    cur.execute(insert_sql, rec)

        # populate Book
        with open(self.book_file) as fh:
            # discard header
            fh.readline()
            
            insert_sql = ''  # TODO add sql here for the Book INSERT
            
            for line in fh:
                rec = line.split('\t')
                if len(rec) == 4:
                    try:
                        cur.execute(insert_sql, rec)
                    except sqlite3.IntegrityError:
                        print line

        self.conn.commit()
    
    
    def search_titles(self, title):
        '''Look for Books with title like query'''
        
        # new cursor
        cur = self.conn.cursor()
        
        # sql statement                             TODO: try modifying me!
        sql = '''
        SELECT 
            Book.book_id, 
            Author.last_name, 
            Author.first_name, 
            Book.title, 
            Book.pub
        FROM 
            Book JOIN Author 
        USING 
            (auth_id)
        WHERE
            Book.title LIKE ?
        '''
        
        cur.execute(sql, (title,))
    
        return cur.fetchall()
        
# main code block
if __name__ == '__main__':
    # get database, tsv from arguments
    
    db = LibraryDB(DB_FILE, AUTH_FILE, BOOK_FILE)
    
    try:
        results = db.search_titles(sys.argv[1])
        
        for rec in results:              # TODO: try displaying different info
                                         #       in the record output
            bk_id, auth_ln, auth_fn, bk_title, bk_pub = rec
            print "{}. {} {}, {} ({})".format(
                bk_id, auth_fn, auth_ln, bk_title, bk_pub
            )
        
    except IndexError:
        print "Usage: {} title".format(sys.argv[0])
    