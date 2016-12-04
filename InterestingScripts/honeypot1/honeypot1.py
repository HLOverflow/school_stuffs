#!/usr/bin/python
import re
import socket

fo = open("login.html", "r")
fakeLogin=fo.read()
fo.close()

okMessage='''HTTP/1.1 200 OK
Date: Wed, 10 Oct 2016 16:02:54 GMT
Server: Apache/2.4.18 (Debian)
Last-Modified: Tue, 27 Sep 2016 12:41:29 GMT
ETag: "2b60-53d7c904ef65a"
Accept-Ranges: bytes
Content-Length: 11104
Vary: Accept-Encoding
Connection: close
Content-Type: text/html


'''

badMessage='''HTTP/1.1 400 Bad Request
Date: Mon, 10 Oct 2016 14:10:58 GMT
Server: Apache/2.4.18 (Debian)
Content-Length: 301
Connection: close
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>400 Bad Request</title>
</head><body>
<h1>Bad Request</h1>
<p>Your browser sent a request that this server could not understand.<br />
</p>
<hr>
<address>Apache/2.4.18 (Debian) Server at 127.0.1.1 Port 80</address>
</body></html>
'''

userInput = raw_input()
regex = re.compile(".* /.*HTTP/.*")
if regex.findall(userInput):
	print okMessage
	print fakeLogin
else:
	print badMessage


