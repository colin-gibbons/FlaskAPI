#!/usr/bin/env python3
#

Not working code
ef setUpClass(cls):
    install( level='DEBUG' )
    host = 'localhost'
    # here you can edit your base url
    
    cls.ApiUrl = "http://localhost:8000/"
    # here you can edit your database connection credentials
    
    cls.db = connect( host=host,
                      user='username',
                      password='password',
                      database='password' )
@classmethod
def tearDownClass(cls):
    cls.db.close( )
    print("------test is over------")
  
