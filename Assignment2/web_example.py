from http.server import HTTPServer, BaseHTTPRequestHandler
 
host = ('localhost', 4242)
 
class MyResquest(BaseHTTPRequestHandler):
    timeout = 5
    server_version = "Apache"

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")  # HTTP header
        self.end_headers()

        with open("web/example.html","r",encoding="utf-8") as f:
            html = f.read()

        self.wfile.write(html.encode())  

    def do_POST(self):
        post_data = self.rfile.read(int(self.headers['content-length']))    # Read from post
        print(post_data.decode())
 
        self.send_response(200)
        self.send_header("Content-type","text/html")    # Set response header
        self.end_headers()
 
        html = '''<!DOCTYPE HTML>
        <html>
            <head>
                <title>Post page</title>  
            </head>
            <body>
                Post Data:%s  <br />
            </body>
        </html>''' %post_data
        self.wfile.write(html.encode())
 
if __name__ == '__main__':
    server = HTTPServer(host, MyResquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()