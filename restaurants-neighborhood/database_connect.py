## simple demo script for showing how to connect to an sqlite DB 
# from Python, and run a simple SQL query 

# import the python library for SQLite 
import sqlite3

def getRestosFromNeighborhood(neighborhood_name):
    # connect to the database file, and create a connection object
    db_connection = sqlite3.connect('restaurants.db')

    # create a database cursor object, which allows us to perform SQL on the database. 
    db_cursor = db_connection.cursor()

    # run a first query 
    #db_cursor.execute("SELECT from neighborhoods")
    db_cursor.execute("""SELECT * from restaurants
                        INNER JOIN neighborhoods ON restaurants.NEIGHBORHOOD_ID=neighborhoods.ID
                        WHERE neighborhoods.NAME="%s"
                        """ % neighborhood_name)

    # store the result in a local variable. 
    # this will be a list of tuples, where each tuple represents a row in the table
    list_restaurants = db_cursor.fetchall()

    db_connection.close()
    #print("list_restaurants contents:")
    return(list_restaurants)

def getdata():
    # connect to the database file, and create a connection object
    db_connection = sqlite3.connect('restaurants.db')

    # create a database cursor object, which allows us to perform SQL on the database. 
    db_cursor = db_connection.cursor()

    # run a first query 
    #db_cursor.execute("SELECT from neighborhoods")
    db_cursor.execute("""SELECT * from restaurants
                        INNER JOIN neighborhoods ON restaurants.NEIGHBORHOOD_ID=neighborhoods.ID
                        WHERE neighborhoods.NAME="Kreuzberg"
                        """)

    # store the result in a local variable. 
    # this will be a list of tuples, where each tuple represents a row in the table
    list_restaurants = db_cursor.fetchall()

    db_connection.close()
    #print("list_restaurants contents:")
    return(list_restaurants)

def getNeighborhoods():
        # connect to the database file, and create a connection object
    db_connection = sqlite3.connect('restaurants.db')

    # create a database cursor object, which allows us to perform SQL on the database. 
    db_cursor = db_connection.cursor()

    # run a first query 
    #db_cursor.execute("SELECT from neighborhoods")
    db_cursor.execute("""SELECT * from neighborhoods
                        """)

    # store the result in a local variable. 
    # this will be a list of tuples, where each tuple represents a row in the table
    list_neighborhoods = db_cursor.fetchall()

    db_connection.close()
    return(list_neighborhoods)
