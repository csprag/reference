curl
-------

curl is a command line web browser tool. However, instead of rendering html to form web pages, curl will print out the infomation in the terminal. curl is useful for transferring data to or from a server. 

~~~ bash
$ curl https://csprag.herokuapp.com
<!DOCTYPE html>
<html lang="en">
...
<!-- HTML for home page of EECS 201 site -->
...
</html>
~~~

---


#### Basic Usage
~~~ bash
$ curl <url>
~~~

---

### Useful Options / Examples

#### `curl --request <method> <url>`

This command will allow you to select the request method to send to the server.

~~~ bash
$ curl --request GET https://csprag.herokuapp.com
<!DOCTYPE html>
<html lang="en">
...
<!-- HTML for home page of EECS 201 site -->
...
</html>
~~~

#### `curl -o <filename> <url>` 

This command will save the results of the curl command to a predefined file.

~~~ bash
$ curl -o --request GET EECS201.txt https://csprag.herokuapp.com
$ cat EECS201.txt
<!DOCTYPE html>
<html lang="en">
...
<!-- HTML for home page of EECS 201 site -->
...
</html>
~~~

#### `curl -O <filename> <url>` 

This command will download the file at the specified url address with the original file name.

~~~ bash
$ curl -O https://csprag.herokuapp.com/static/adv/csp-wk5-advanced.pdf
~~~

#### `curl -I <url>` 

This command will only fetch the HTTP request headers of a particular page.
~~~ bash
$ curl -I --request GET https://csprag.herokuapp.com
HTTP/1.1 200 OK
Connection: keep-alive
Server: gunicorn/19.9.0
Date: Sun, 10 Feb 2019 16:59:39 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 11372
Via: 1.1 vegur
~~~

#### `curl --verbose <url>` 

This command will print all HTTP request information and headers.
~~~ bash
$ curl -I --verbose https://csprag.herokuapp.com
* Rebuilt URL to: https://csprag.herokuapp.com/
*   Trying 35.175.30.164...
* TCP_NODELAY set
* Connected to csprag.herokuapp.com (35.175.30.164) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* Cipher selection: ALL:!EXPORT:!EXPORT40:!EXPORT56:!aNULL:!LOW:!RC4:@STRENGTH
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/cert.pem
CApath: none
* TLSv1.2 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Client hello (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS change cipher, Client hello (1):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN, server did not agree to a protocol
* Server certificate:
*  subject: C=US; ST=California; L=San Francisco; O=Heroku, Inc.; CN=*.herokuapp.com
*  start date: Apr 19 00:00:00 2017 GMT
*  expire date: Jun 22 12:00:00 2020 GMT
*  subjectAltName: host "csprag.herokuapp.com" matched cert's "*.herokuapp.com"
*  issuer: C=US; O=DigiCert Inc; OU=www.digicert.com; CN=DigiCert SHA2 High Assurance Server CA
*  SSL certificate verify ok.
> HEAD / HTTP/1.1
> Host: csprag.herokuapp.com
> User-Agent: curl/7.54.0
> Accept: */*
> 
< HTTP/1.1 200 OK
HTTP/1.1 200 OK
< Connection: keep-alive
Connection: keep-alive
< Server: gunicorn/19.9.0
Server: gunicorn/19.9.0
< Date: Sun, 10 Feb 2019 17:04:57 GMT
Date: Sun, 10 Feb 2019 17:04:57 GMT
< Content-Type: text/html; charset=utf-8
Content-Type: text/html; charset=utf-8
< Content-Length: 11372
Content-Length: 11372
< Via: 1.1 vegur
Via: 1.1 vegur

< 
* Connection #0 to host csprag.herokuapp.com left intact
~~~

#### `curl -L <url>`

This command will instruct curl to follow redirects until it reaches its final destination.

If you try to curl google.com, you will get a redirect message because the specified location has moved:
~~~ bash
$ curl google.com
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
~~~


If you curl google.com with redirects enabled, curl will navigate to www.google.com:
~~~ bash
$ curl -L google.com
<!DOCTYPE html>
<html lang="en">
...
<!-- HTML for www.google.com -->
...
</html>
~~~
