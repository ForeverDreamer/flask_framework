from html import escape
from werkzeug.wrappers import Request, Response
from werkzeug.formparser import parse_form_data


@Request.application
def hello_world1(request):
    result = ['<title>Greeter</title>']
    if request.method == 'POST':
        result.append(f"<h1>Hello {escape(request.form['name'])}!</h1>")
    result.append('''
        <form action="" method="post">
            <p>Name: <input type="text" name="name" size="20">
            <input type="submit" value="Greet me">
        </form>
    ''')
    return Response(''.join(result), mimetype='text/html')


def hello_world2(environ, start_response):
    result = ['<title>Greeter</title>']
    if environ['REQUEST_METHOD'] == 'POST':
        form = parse_form_data(environ)[1]
        result.append(f"<h1>Hello {escape(form['name'])}!</h1>")
    result.append('''
        <form action="" method="post">
            <p>Name: <input type="text" name="name" size="20">
            <input type="submit" value="Greet me">
        </form>
    ''')
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [''.join(result).encode('utf-8')]
