#!/bin/bash
cd /tmp
export FLASK_APP=backend.py 
mkdir -p /tmp/nginx/cache
nginx&
flask run
 

