# stdlib
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
import socket
import SocketServer
import struct
from urlparse import urlparse, parse_qs

# 3rd party
import datadog
import redis

# Initialize the Dogstatsd client
from datadog import initialize, statsd
initialize(statsd_use_default_route=True)

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    @statsd.timed("meetup.guestbook.response_time")
    def do_GET(self):
        self._set_headers()

        if self.path == "/controllers.js":
            # Return the JS

            with open("controllers.js") as f:
                self.wfile.write(f.read())
        
        elif self.path.startswith("/guestbook"):
            args = parse_qs(urlparse(self.path).query)
            cmd = args.get("cmd", [None])[0]
            key = args.get("key", [None])[0]
            val = args.get("value", [None])[0]
            r = redis.Redis(host=os.environ.get("REDIS_MASTER_SERVICE_HOST"), port=6379)

            if cmd == "set":
                r.set(key, val)
                self.wfile.write('{"message": "Updated"}')
                statsd.increment("meetup.guestbook.cmd", tags=["cmd:set"])

            else:
                val = r.get(key)
                self.wfile.write('{"data": "%s"}' % val)
                statsd.increment("meetup.guestbook.cmd", tags=["cmd:get"])

        else:
            # We return the HTML
            with open("index.html") as f:
                self.wfile.write(f.read())

    def do_HEAD(self):
        self._set_headers()

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()