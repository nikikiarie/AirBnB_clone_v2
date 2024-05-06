#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install ngnix
sudo ufw allow 'Ngnix HTTP'

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
   Holberton School
  </body>
  </html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/ngnix/sites-enabled/default
sudo service ngnix restart
