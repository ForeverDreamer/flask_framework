# 1 WSGI Environment
from werkzeug.test import create_environ
from werkzeug.wrappers import Request
from werkzeug.wrappers import Response
from io import StringIO

environ = create_environ('/foo', 'http://localhost:8080/')
print(environ['PATH_INFO'])
print(environ['SCRIPT_NAME'])
print(environ['SERVER_NAME'])
print('--------------------------------------------------')

# 2 Enter Request
request = Request(environ)
print(request.path)
print(request.script_root)
print(request.host)
print(request.url)
print(request.method)
print('--------------------------------------------------')

data = "name=this+is+encoded+form+data&another_key=another+one"
request = Request.from_values(
    query_string='foo=bar&blah=blafasel',
    content_length=len(data),
    input_stream=StringIO(data),
    content_type='application/x-www-form-urlencoded',
    method='POST'
)
print(request.method)
print(request.args.keys())
print(request.args['blah'])
print(request.form['name'])
print(request.headers['Content-Length'])
print(request.headers['Content-Type'])
print('--------------------------------------------------')

# 3 Header Parsing
environ = create_environ()
environ.update(
    HTTP_ACCEPT='text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    HTTP_ACCEPT_LANGUAGE='de-at,en-us;q=0.8,en;q=0.5',
    HTTP_ACCEPT_ENCODING='gzip,deflate',
    HTTP_ACCEPT_CHARSET='ISO-8859-1,utf-8;q=0.7,*;q=0.7',
    HTTP_IF_MODIFIED_SINCE='Fri, 20 Feb 2009 10:10:25 GMT',
    HTTP_IF_NONE_MATCH='"e51c9-1e5d-46356dc86c640"',
    HTTP_CACHE_CONTROL='max-age=0'
)
request = Request(environ)
print(request.accept_mimetypes.best)
print('application/xhtml+xml' in request.accept_mimetypes)
print(request.accept_mimetypes["application/json"])
print(request.accept_languages.best)
print([v for v in request.accept_languages.values()])
print('gzip' in request.accept_encodings)
print(request.accept_charsets.best)
print('utf-8' in request.accept_charsets)
print('UTF8' in request.accept_charsets)
print('de_AT' in request.accept_languages)
print(request.if_modified_since)
print(request.if_none_match)
print(request.cache_control)
print(request.cache_control.max_age)
print('e51c9-1e5d-46356dc86c640' in request.if_none_match)
print('--------------------------------------------------')

# 4 Responses
response = Response("Hello World!")
print(response.headers['content-type'])
print(response.data)
print(response.status)
response.headers['content-length'] = len(response.data)
print(response.status)
response.status = '404 Not Found'
print(response.status_code)
print('--------------------------------------------------')
