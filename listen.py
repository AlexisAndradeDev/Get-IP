from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # get IP from header 'X-Forwarded-For' if it exists
        x_forwarded_for = self.headers.get('X-Forwarded-For')
        if x_forwarded_for:
            client_ip = x_forwarded_for.split(',')[0].strip()
        else:
            client_ip = self.client_address[0]
        
        print(f"IP of the emisor of the request: {client_ip}")
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Request received\n")

if __name__ == "__main__":
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Listening on port 8080...")
    httpd.serve_forever()