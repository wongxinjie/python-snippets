from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):

    def get_content_type(self, filename):
        types = {
            "txt": "text/plain; charset=utf-8",
            "jpg": "image/jpeg",
            "jpeg": "image/jpeg"
        }
        subfix = filename.split(".", -1)[-1]
        return types.get(subfix, "text/html; charset=utf-8")

    def do_GET(self):
        try:
            filename = self.path[1:]
            content_type = self.get_content_type(filename)
            if content_type.startswith("image"):
                reader = open(filename, 'rb')
                content = reader.read()
            else:
                reader = open(filename, 'r')
                content = reader.read().encode('utf-8')
            reader.close()

            self.send_response(200)
            self.send_header('Content-Type', content_type)
            self.end_headers()
            self.wfile.write(content)
        except IOError as err:
            self.send_error(404, "File Not Found: %s" % self.path)


def main():
    try:
        server = HTTPServer(('', 8080), Handler)
        print("Running server on %s" % 8080)
        server.serve_forever()
    except KeyboardInterrupt as err:
        server.socket.close()


if __name__ == "__main__":
    main()
