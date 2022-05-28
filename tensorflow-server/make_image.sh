#!/bin/sh
docker run -d --rm --name serving_base tensorflow/serving
docker cp $pwd/test serving_base:/models/test
docker commit --change "ENV MODEL_NAME test" serving_base my_server_tf
docker kill serving_base

# docker -p 8501:8051 my_server_tf 로 컨테이너 생성
