#!/usr/bin/env python3
import os, json
import cgitb
import cgi
import templates
import secret
cgitb.enable()
print("Content-type:text/html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>Hello WOrld !</p>")

#Q1
print(os.environ)
json_object = json.dumps(dict(os.environ), indent = 4)
print(json_object)

#Q2
for param in os.environ.keys():
    if (param == "QUERY_STRING"):
        # print(f"<em>{param}</em> = {os.environ[param]} </li>")
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

# Q3
for param in os.environ.keys():
    if (param == "HTTP_USER_AGENT"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))


# form = cgi.FieldStorage()
# if "name" not in form or "addr" not in form:
#     print("<H1>Error</H1>")
#     print("Please fill in the name and addr fields.")

# print("<p>name:", form["name"].value)
# print("<p>addr:", form["addr"].value)

print(templates.login_page())
'''
import sys
posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    print(f"<p> POSTED: <pre>")
    for line in posted.splitlines():
        print(line)
    print("</pre></p>")

'''