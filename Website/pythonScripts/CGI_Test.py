from flask import Flask, render_template

form = cgi.FieldStorage()

image = form.getValue("inputFile")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head")
print("<body>")
print("<h2>Image file: %s </h2>")
print("</body>")
print("</html")