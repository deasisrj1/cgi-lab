#!/usr/bin/env python3

import templates
import cgitb
import cgi
import templates
import secret
import os

cgitb.enable()
form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')


if username == secret.username and password == secret.password:
    print("Set-Cookie:username = %s;" % username)
    print("Set-Cookie:password = %s;" % password)
    print("Set-Cookie:Expires = Tuesday, 31-Dec-2022 23:12:40 GMT;")
    print("Set-Cookie:Domain = http://localhost:8080/")
    print("Content-type:text/html\r\n")
    print()
    print(templates.secret_page(username=username, password=password))
else:
    print(templates.after_login_incorrect())