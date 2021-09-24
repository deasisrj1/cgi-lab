#!/usr/bin/env python3
import os

def test_cookies():
    print("Set-Cookie:UserID = XYZ;")
    print("Set-Cookie:Password = XYZ123;")
    print("Set-Cookie:Expires = Tuesday, 31-Dec-2022 23:12:40 GMT;")
    print("Set-Cookie:Domain = www.tutorialspoint.com;")
    print("Content-type:text/html\r\n")
    print('<html>')
    print('<head>')
    print('<title>COOKIES SET - First CGI Program </title>')
    print('</head>')
    print('<body>')
    print('<h2>ALL DONE!</h2>')
    print('</body>')
    print('</html>')

    # print(os.environ)
    for param in os.environ.keys():
        if (param=="HTTP_COOKIE"):
            print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

test_cookies()
for param in os.environ.keys():
    if (param=="HTTP_COOKIE"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))