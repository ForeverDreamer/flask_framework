# HTTP Related
from werkzeug.datastructures import Headers
d = Headers()
d.add('Content-Type', 'text/plain')
d.add('Content-Disposition', 'attachment', filename='foo.png')
