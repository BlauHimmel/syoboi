import BaseHTTPServer
import cgi

import worm


class WebRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/before":
            print "get before data..."
            data = worm.get_before()
            print data
            self.send_response(200)
            self.send_header('Content-type', 'application/json;charset=utf-8')
            self.end_headers()
            self.wfile.write(data.encode("utf-8"))
        elif self.path == "/today":
            print "get today data..."
            data = worm.get_today()
            print data
            self.send_response(200)
            self.send_header('Content-type', 'application/json;charset=utf-8')
            self.end_headers()
            self.wfile.write(data.encode("utf-8"))
        elif self.path == "/tomorrow":
            print "get tomorrow data..."
            data = worm.get_tomorrow()
            print data
            self.send_response(200)
            self.send_header('Content-type', 'application/json;charset=utf-8')
            self.end_headers()
            self.wfile.write(data.encode("utf-8"))
        else:
            print "error 404 not found..."
            self.send_error(404)

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.getheader('content-length'))
            postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}
        data = postvars["url"]
        data = data[0]
        if data is None:
            self.send_response(200)
            self.wfile.write("error")
        if self.path == "/detail_basic":
            print "get basic detail from ",data
            res = worm.get_detail_basic(data)
            print res
            self.send_response(200)
            self.send_header('Content-type', 'application/json;charset=utf-8')
            self.end_headers()
            self.wfile.write(res.encode("utf-8"))
        elif self.path == "/detail_staff":
            print "get staff detail from ", data
            res = worm.get_detail_staff(data)
            print res
            self.send_response(200)
            self.send_header('Content-type', 'application/json;charset=utf-8')
            self.end_headers()
            self.wfile.write(res.encode("utf-8"))
        elif self.path == "/detail_cast":
            print "get cast detail from ", data
            res = worm.get_detail_cast(data)
            print res
            self.send_response(200)
            self.send_header('Content-type', 'application/json;charset=utf-8')
            self.end_headers()
            self.wfile.write(res.encode("utf-8"))
        else:
            print "error 404 not found..."
            self.send_error(404)


server = BaseHTTPServer.HTTPServer(("120.25.222.223", 8080), WebRequestHandler)
server.serve_forever()