from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<html>
<head>
<title> My Web Server</title>
</head>
<body bgcolor="cyan">
<table border="1" align="center" cellpadding="10">
                <caption><h3>List of Protocols</h3></caption>
                <tr><th>S.no</th><th>Name of the layers</th><th>Name of the protocols</th></tr>
                <tr><td>1</td><td>Application Layer</td><td>HTTP, FTP, TELNET, DHCP, DNS</td></tr>
                <tr><td>2</td><td>Transport Layer</td><td>TCP & UDP</td></tr>
                <tr><td>3</td><td>Network/Interent Layer</td><td>ICMP, IGMP, ARP, IPv4</td></tr>
                <tr><td>4</td><td>Data Link/Network Access Layer</td><td>Ethernet</td></tr>
            </table>
</body>
</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()