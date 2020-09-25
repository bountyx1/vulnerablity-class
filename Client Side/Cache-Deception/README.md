## Web Cache Deception

- Interesting username:user.css what will happen if 
GET /api/me/user.css
- Absence of cache Header may lead to caching by cdn
-  Proxy server/CDN May override  the cache  control headers and cache even if site has 
“**Pragma**: no-cache,**Cache-Control**: no-store

- Cloudfare mitigation also checks for content type

- website may enable Cache on basis of specific parameter and Header ?cache=true [:rare]

### Cache status header:
- CF-Cache-Status(Cloudfare),
-  X-Cache-Status(Nginx)
- X-Varnish
- X-Cache cloudfront


### Important Cache Header
- Cache-Control:**public** [Cachable by **proxy+browser**]
- Cache-Control:**private** [**Browser** only]
- **max-age** max timespan of cache client side
- Expires sets date 
``` If both Expires and max-age are set max-age will take precedence.```
- **ETag**- if browser-cache(md5) == **If-None-Match**:Server(md5) up to date return 304 means cache uptodate
- **If-Modified-Since Last-Modified **(Simliar as Etag except it uses date)


### Exploitation
- example.com/myhome/dashboard.css url(r'^/myhome/dashboard')
- example.com/myhome/dashboard/nonexisting.css (r'^/myhome/dashboard/')
- with PATH_INFO enabled file.php/nonexisting.css
- creating username with navjeet.css when GET /api/user/navjeet.css
- Asp.net FriendlyURLs means site.com/home.aspx  will allow without extension site.com/home returns same content 
- **Path Confusion**
    ```- \n /account.php%0Anonexistent.css
     ; /account.php%3Bnonexistent.css
    - # / account.php%23nonexistent.css
    - ? account.php%3Fname=valnonexistent.css```


### Mitigation
- Store static file in seperate dir and cache only them like images/*.css
- cache on basis of content-type
- Disable features that could result in confusion about the file extension between the proxy server and the origin server (e.g. AcceptPathInfo, overly broad rewrite rules, etc.).

### Terminology
- **PATH_INFO** : environment variable set by Apache when the AcceptPathInfo directive is turned on. It will contain trailing pathname information that follows an actual filename or non-existent file in an existing directory, whether the request is accepted or rejected. Environment variables are then passed on to the Apache/CGI module in charge of rendering the page.
- Eg-test/here.html only file in test dir but test/here.html/more valid too

### Reference
- [How cloudfare caching works](https://medium.com/cloudflare-blog/understanding-our-cache-and-the-web-cache-deception-attack-69768040f90e)
- [Varnish cache status](https://www.getpagespeed.com/server-setup/varnish/cache-status-check)
- [Apache Pathinfo Configuration](https://www.a2hosting.in/kb/developer-corner/apache-web-server/pathname-information-and-acceptpathinfo-directive)
- [Nginx Configuration](https://www.nginx.com/resources/wiki/start/topics/examples/phpfcgi/)
- [override cache-control](https://www.nginx.com/blog/nginx-caching-guide/)
[Webcache deception](https://www.blackhat.com/docs/us-17/wednesday/us-17-Gil-Web-Cache-Deception-Attack-wp.pdf)
[Cached and Confused: Web Cache Deception in the Wild](https://sajjadium.github.io/files/usenixsec2020wcd_paper.pdf)


