from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from html import escape

# 1 Environment Dictionary
# def application(environ, start_response):
#     # Sorting and stringifying the environment key, value pairs
#     response_body = [
#         '%s: %s' % (key, value) for key, value in sorted(environ.items())
#     ]
#     response_body = '\n'.join(response_body)
#
#     status = '200 OK'
#     response_headers = [
#         ('Content-Type', 'text/plain'),
#         ('Content-Length', str(len(response_body)))
#     ]
#     start_response(status, response_headers)
#
#     return [response_body.encode(encoding='utf-8')]


# 2 Response Iterable
# def application(environ, start_response):
#     response_body = [
#         '%s: %s' % (key, value) for key, value in sorted(environ.items())
#     ]
#     response_body = '\n'.join(response_body)
#
#     # Adding strings to the response body
#     response_body = [
#         'The Beggining\n',
#         '*' * 30 + '\n',
#         response_body,
#         '\n' + '*' * 30,
#         '\nThe End'
#     ]
#
#     # So the content-lenght is the sum of all string's lengths
#     content_length = sum([len(s) for s in response_body])
#
#     status = '200 OK'
#     response_headers = [
#         ('Content-Type', 'text/plain'),
#         ('Content-Length', str(content_length))
#     ]
#
#     start_response(status, response_headers)
#     return [s.encode(encoding='utf-8') for s in response_body]


# # Instantiate the server
# httpd = make_server(
#     'localhost',  # The host name
#     8051,  # A port number where to wait for the request
#     application  # The application object name, in this case a function
# )
#
# # Wait for a single request, serve it and quit
# httpd.handle_request()


# 3 Parsing the Request - Get
# html = """
# <html>
# <body>
#    <form method="get" action="">
#         <p>
#            Age: <input type="text" name="age" value="%(age)s">
#         </p>
#         <p>
#             Hobbies:
#             <input
#                 name="hobbies" type="checkbox" value="software"
#                 %(checked-software)s
#             > Software
#             <input
#                 name="hobbies" type="checkbox" value="tunning"
#                 %(checked-tunning)s
#             > Auto Tunning
#         </p>
#         <p>
#             <input type="submit" value="Submit">
#         </p>
#     </form>
#     <p>
#         Age: %(age)s<br>
#         Hobbies: %(hobbies)s
#     </p>
# </body>
# </html>
# """
#
#
# def application(environ, start_response):
#     # Returns a dictionary in which the values are lists
#     d = parse_qs(environ['QUERY_STRING'])
#
#     # As there can be more than one value for a variable then
#     # a list is provided as a default value.
#     age = d.get('age', [''])[0]  # Returns the first age value
#     hobbies = d.get('hobbies', [])  # Returns a list of hobbies
#
#     # Always escape user input to avoid script injection
#     age = escape(age)
#     hobbies = [escape(hobby) for hobby in hobbies]
#
#     response_body = html % {  # Fill the above html template in
#         'checked-software': ('', 'checked')['software' in hobbies],
#         'checked-tunning': ('', 'checked')['tunning' in hobbies],
#         'age': age or 'Empty',
#         'hobbies': ', '.join(hobbies or ['No Hobbies?'])
#     }
#
#     status = '200 OK'
#
#     # Now content type is text/html
#     response_headers = [
#         ('Content-Type', 'text/html'),
#         ('Content-Length', str(len(response_body)))
#     ]
#
#     start_response(status, response_headers)
#     return [response_body.encode(encoding='utf-8')]


html = """
<html>
<body>
   <form method="post" action="">
        <p>
           Age: <input type="text" name="age" value="%(age)s">
        </p>
        <p>
            Hobbies:
            <input
                name="hobbies" type="checkbox" value="software"
                %(checked-software)s
            > Software
            <input
                name="hobbies" type="checkbox" value="tunning"
                %(checked-tunning)s
            > Auto Tunning
        </p>
        <p>
            <input type="submit" value="Submit">
        </p>
    </form>
    <p>
        Age: %(age)s<br>
        Hobbies: %(hobbies)s
    </p>
</body>
</html>
"""


def application(environ, start_response):
    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_body_size = 0

    # When the method is POST the variable will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    request_body = environ['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)

    age = d.get('age', [''])[0]  # Returns the first age value.
    hobbies = d.get('hobbies', [])  # Returns a list of hobbies.

    # Always escape user input to avoid script injection
    age = escape(age)
    hobbies = [escape(hobby) for hobby in hobbies]

    response_body = html % {  # Fill the above html template in
        'checked-software': ('', 'checked')['software' in hobbies],
        'checked-tunning': ('', 'checked')['tunning' in hobbies],
        'age': age or 'Empty',
        'hobbies': ', '.join(hobbies or ['No Hobbies?'])
    }

    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body.encode(encoding='utf-8')]


httpd = make_server('localhost', 8051, application)

# Now it is serve_forever() in instead of handle_request()
httpd.serve_forever()
