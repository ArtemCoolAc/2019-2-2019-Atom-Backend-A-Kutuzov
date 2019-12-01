def app(environ, start_response):
    data = b'Hellom Bob\n'
    headers = [('Content-Type', 'text/plain'),
              ('Content-Length', str(len(data)))]
    start_response('200 OK', headers)
    return [data]
