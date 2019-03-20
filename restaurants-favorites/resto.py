#!/usr/local/bin/python3

from database_connect import getRestosFromNeighborhood, getNeighborhoods, insertUser
import cgi

# Get the neighborhood entered in the form
# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'neighborhood'
user_name = form.getvalue('name')

# get an input filed from the form called 'neighborhood'
neighborhood_id = form.getvalue('neighborhood')

# add the user's name and neighborhood id to the users table
insertUser(user_name, neighborhood_id)

neighborhoods_data = getNeighborhoods()

# default neighborhood name BEFORE the correct name is matched
neighborhood_name = "unknown"

# For each item in the database result
# check which name is for this neighborhood
for item in neighborhoods_data:
    if item[0] == int(neighborhood_id):
        neighborhood_name = item[1]

# Retrieve the database data
# Example result
# [
#     (1, 'Curry 36', 1, 1, 1, 'Kreuzberg'),
#     (3, 'Knofi', 1, 2, 1, 'Kreuzberg')
# ]
restaurants_data = getRestosFromNeighborhood(neighborhood_id)

# Create an empty string to build the html bullet points
restaurants_list = ""

# For each item in the database result
# add it to the string with the html tags
for item in restaurants_data:
    restaurants_list += "<li>" + item[1] + "</li>\n"

# Send the response
print("""
    <html>
    <body>
    <h1>Restaurants in %s</h1>
    <ul>
    %s
    </ul>
    </body>
    </html>
    """ % (neighborhood_name, restaurants_list))