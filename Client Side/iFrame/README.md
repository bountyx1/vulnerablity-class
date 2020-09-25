docker pull tomcat
docker run -it --rm -p 8080:8080  -v  /path/:/usr/local/tomcat/webapps tomcat
