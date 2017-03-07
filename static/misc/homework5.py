#!/usr/bin/env python
'''A frontend for the CMOA catalog'''

# Import statements

import tornado.ioloop
import tornado.web
                             # TODO: import the CMOAdb class from homework4


# Class definitions
#  Handlers:

class MainHandler(tornado.web.RequestHandler):
    '''Front page for the site'''
    
    def get(self):
        self.render("query.html")


class SearchHandler(tornado.web.RequestHandler):
    '''Perform a search'''
    
    def initialize(self, db):
        self.db = db

    def get(self):
        field =              # TODO: get the user-selected column to search
        search_string =      # TODO: get the user-entered search string
        
        rows =               # TODO: call the get_artthings() method
                             #       using `field` and `search_string`
        
        self.render("results.html", rows=rows)


# main code block

if __name__ == "__main__":
    db =                     # TODO: create a new database connection
                             #       using CMOAdb. Pass it names for the
                             #       sqlite file and the json file.
    
    # create app, register handlers
    app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/search", SearchHandler, {'db': db}),
    ], debug=True)

    # run the app
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
