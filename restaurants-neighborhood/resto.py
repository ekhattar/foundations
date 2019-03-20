#!/usr/local/bin/python3

from database_connect import getRestosFromNeighborhood
import cgi

# Get the neighborhood entered in the form
# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'neighborhood'
neighborhood_name = form.getvalue('neighborhood')

# Retrieve the database data
# Example result
# [
#     (1, 'Curry 36', 1, 1, 1, 'Kreuzberg'),
#     (3, 'Knofi', 1, 2, 1, 'Kreuzberg')
# ]
restaurants_data = getRestosFromNeighborhood(neighborhood_name)

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