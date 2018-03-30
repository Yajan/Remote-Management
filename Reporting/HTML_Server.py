from http.server import HTTPServer,BaseHTTPRequestHandler
import webbrowser
class Serve(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path == 'C:/Users/Yajana/PycharmProjects/Distributed-setup-4/Reporting/report.html'

        if self.path == '/api':
            self.path == "C:/Users/Yajana/PycharmProjects/Distributed-setup-4/Data/data.json"

        try:
            file_to_open = open(self.path).read()
            self.send_response(200)

        except:
            file_to_open = open("C:/Users/Yajana/PycharmProjects/Distributed-setup-4/Data/data.json").read()
            self.send_response(404)

        self.end_headers()
        self.wfile.write(bytes(file_to_open,'utf-8'))

httpd = HTTPServer(('localhost',80),Serve)
new = 2 # open in a new tab, if possible

# open a public URL, in this case, the webbrowser docs
url = "localhost/api"

webbrowser.open(url,new=new,)
httpd.serve_forever()




