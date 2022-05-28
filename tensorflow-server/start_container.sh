#!/bin/sh
docker run -p 8501:8501 --mount type=bind,source=$PWD/test,target=/models/test -e MODEL_NAME=test -td tensorflow/serving