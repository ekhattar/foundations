#!/usr/local/bin/python3

import csv
import cgi


# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'name'
# and assign it's value to a local variable called v_name
form_input = form.getvalue('color')


