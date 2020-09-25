FROM nginx
EXPOSE 80
RUN apt-get update && apt-get install python3 python3-pip -y && apt-get clean
RUN pip3 install flask
COPY lab /tmp/
COPY nginx.conf /etc/nginx/nginx.conf
COPY start.sh /tmp
RUN chmod +x /tmp/start.sh
CMD ["bash","/tmp/start.sh"]
