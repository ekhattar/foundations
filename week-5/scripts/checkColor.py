#!/usr/local/bin/python3

import csv
import cgi

# Read the rows in the color csv file into a new
# dict object where the csv header column names are the keys
# and the row items are the values
with open("color-check/colors.csv") as color_file:
    color_list = [{key: value for key, value in row.items()}
        for row in csv.DictReader(color_file, skipinitialspace = True)]

# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'name'
# and assign it's value to a local variable called v_name
form_input = form.getvalue('color')

is_color = False

# Check if the form input can be found in the color
# names of the color list
for item in color_list:
    item_color = item["color_name"].lower()
    if form_input == item_color:
        is_color = True
        hex_code = item["hex_code"]

# Send a response
# if it's a color, the response text
# will be in the input color
if is_color is True:
    print("""
    <html>
    <body>
    <p style="color: %s">
    SUCCESS: %s is a color
    </p>
    </body>
    </html>
    """ % (hex_code, form_input))
else:
    print("""
    <html>
    <body>
    <p>
    FAILURE: %s is NOT a color
    </p>
    </body>
    </html>
    """ % form_input)
