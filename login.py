#!/usr/bin/env python3

import templates
import cgitb
import cgi
import templates
import secret
cgitb.enable()
form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')

print("Content-Type: text/html")
print()
if username == secret.username and password == secret.password:
    print("Set-Cookie:username = %s;" % username)
    print("Set-Cookie:password = %s;" % password)
    print("Set-Cookie:Expires = Tuesday, 31-Dec-2022 23:12:40 GMT;")
    print(templates.secret_page(username=username, password=password))
else:
    print(templates.after_login_incorrect())