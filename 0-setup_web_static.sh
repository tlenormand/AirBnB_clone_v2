#!/usr/bin/env bash
# 0
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
printf %s "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" >/data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -Rh ubuntu:ubuntu /data
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart
