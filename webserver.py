from http.server import HTTPServer, BaseHTTPRequestHandler
from types import TracebackType

class MainServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/DiagIndex.html'
            try:
                open_file = open(self.path[1:],).read()
                self.send_response(200)
            except:
                open_file = "404 - Not Found"
                self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(open_file, 'utf-8'))

httpd = HTTPServer (('localhost', 8080), MainServer)
httpd.serve_forever()

