#!/bin/sh
docker stop eddit
docker container rm eddit
docker image rm eddit_server:latest