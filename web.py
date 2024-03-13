from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body>
<table border=2>
<tr>
<th>Company</th> <th>Revenue</th> <th>Financial Year</th>
</tr>
<tr>
<td>Micro Soft</td> <td>$86.8</td> <td>2014</td>
</tr>
<tr>
<td>Oracle</td> <td>$37.1</td> <td>2013</td>
</tr>
<tr>
<td>SAP</td> <td>$20.9</td> <td>2013</td>
</tr>
<tr>
<td>Symantec</td> <td>$6.8</td> <td>2013</td>
</tr>
<tr>
<td>VMware</td> <td>$5.2</td> <td>2013</td>
</tr>
</table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()