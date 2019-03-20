#!/usr/local/bin/python3

from database_connect import getNeighborhoods
import cgi

# Retrieve the database data
neighborhoods_data = getNeighborhoods()

# Create an empty string to build the html bullet points
# <input type="radio" name="gender" value="female"> Female<br>
radio_buttons_list = ""

# # For each item in the database result
# # add it to the string with the html tags
for item in neighborhoods_data:
    radio_buttons_list += "<input type=\"radio\" name=\"neighborhood\" value=\"" + item[1] + "\">" + item[1] + "<br>"

# # Send the response
print("""
    <html>
    <body>
    <h1>Choose your neighborhood</h1>
    <form action="/resto.py" method="post">
    %s
    <input type="submit" value="Send">
    </form>
    </body>
    </html>
    """ % radio_buttons_list)