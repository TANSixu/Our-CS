from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
import urllib.parse

host = ('localhost', 4242)

def request_web(url):
    req = urllib.request.Request(url)
    # req.set_proxy(proxy, "https")

    resp = urllib.request.urlopen(req)
    html = resp.read().decode("utf-8")
    print(html)

    return html
 
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
        print(post_data)
 
        self.send_response(200)
        self.send_header("Content-type","text/html")    # Set response header
        self.end_headers()
 
        url_raw = post_data.split("&")[0].split("=")[1]
        url = urllib.parse.unquote(url_raw)
        html = request_web(url)
        
        self.wfile.write(html.encode())
 
if __name__ == '__main__':
    server = HTTPServer(host, MyResquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
    