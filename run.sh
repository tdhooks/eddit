#!/bin/sh
docker build -t eddit_server .
docker run --name eddit -d -p 8000:8000 eddit_server