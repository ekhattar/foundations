#!/usr/local/bin/python3

import csv
from cgi import parse_qs, escape
from wsgiref.simple_server import make_server

# Read the rows in the color csv file into a new
# dict object where the csv header column names are the keys
# # and the row items are the values
# with open("color-check/colors.csv") as color_file:
#     color_list = [{key: value for key, value in row.items()}
#         for row in csv.DictReader(color_file, skipinitialspace = True)]

# COLOR CHECKER

# def color_checker(environ, start_response):
#     parameters = parse_qs(environ.get('QUERY_STRING', ''))
#     form_input = escape(parameters['color'][0])
#     is_color = False
#     # Check if the form input can be found in the color
#     # names of the color list
#     for item in color_list:
#         item_color = item["color_name"].lower()
#         if form_input == item_color:
#             is_color = True
#             hex_code = item["hex_code"]
#     # Send a response
#     # if it's a color, the response text
#     # will be in the input color
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return ['''Hello %(form_input)s
#     ''' % {'form_input': form_input}]

#     # if is_color is True:
#     #     print("""
#     #     <html>
#     #     <body>
#     #     <p style="color: %s">
#     #     SUCCESS: %s is a color
#     #     </p>
#     #     </body>
#     #     </html>
#     #     """ % (hex_code, form_input))
#     # else:
#     #     print("""
#     #     <html>
#     #     <body>
#     #     <p>
#     #     FAILURE: %s is NOT a color
#     #     </p>
#     #     </body>
#     #     </html>
#     #     """ % form_input)

index_html = (open('index.html').read())

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [index_html]

# SERVER
if __name__ == '__main__':
    PORT = 8000
    srv = make_server("localhost", 8000, application)
    print("staring WSGI server at http://127.0.0.1:8000")
    # run the server. To kill it, issue Ctrl + C
    srv.serve_forever()
