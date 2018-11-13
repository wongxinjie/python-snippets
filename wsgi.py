from wsgiref.simple_server import make_server


def application(environ, start_response):
    response_body = [
        "%s: %s" % (key, value) for key, value in sorted(environ.items())
    ]
    values = "\n".join(response_body)
    response_body = [
        'The Begining\n',
        '*' * 30 + '\n',
        values,
        '*' * 30 + '\n',
        '\nThe End\n'
    ]
    content_lenth = sum([len(rv) for rv in response_body])
    response_body = [rv.encode('utf-8') for rv in response_body]

    status = "200 OK"
    response_headers = [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(content_lenth))
    ]
    start_response(status, response_headers)

    return response_body


httpd = make_server(
    "127.0.0.1",
    8051,
    application
)

while True:
    httpd.handle_request()
