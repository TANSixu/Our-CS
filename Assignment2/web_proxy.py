from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
import urllib.parse

host = ('localhost', 4242)

 
class MyResquest(BaseHTTPRequestHandler):
    timeout = 5
    server_version = "Apache"

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")  # HTTP header
        self.end_headers()

        with open("web/index.html","r",encoding="utf-8") as f:
            html = f.read()

        self.wfile.write(html.encode())  

    def do_POST(self):
        post_data = self.rfile.read(int(self.headers['content-length'])).decode()    # Read from post
        
 
if __name__ == '__main__':
    server = HTTPServer(host, MyResquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
    