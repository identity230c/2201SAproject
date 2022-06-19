# 디렉토리 구조
```bash 
app 
├── controls
│ ├── Canvas.py 
│ └── UploadImg.py 
├── models 
│ ├── ImgModel.py 
│ └── TfModel.py 
├── Views 
│ ├── canvasPage.html 
│ ├── errInfo.html 
│ ├── index.html 
│ ├── resultPage.html 
│ └── uploadPage.html 
├── static 
│ ├── images 
│ ├── js 
│ └── css 
└ __init__.py
```
### 그 외 디렉토리들
- testImg 디렉토리에는 MNIST 테스트 이미지만 있습니다. 
- tensorflow-server 디렉토리에는 tensorflow-serving 위에 올라간 머신러닝 모델과, docker image 패키징을 위한 쉘 스크립트가 있습니다. 
### 그 외 파일들 
- dockerfile은 flask app을 이미지로 build하기 위한 파일입니다. 
- docker-compose.yml은 localhost에서 개발 중 테스트를 위해 사용하는 파일입니다.
- for-swarm-mode.yml은 docker swarm manager node에서 service를 자동으로 실행하기 위해 사용하는 파일입니다. 
# docker hub링크 
- https://hub.docker.com/repository/docker/identity230c/sa_server_flask
	- flask_app 이미지
- https://hub.docker.com/repository/docker/identity230c/my_server_tf
	- tensorflow serving 이미지 
- https://github.com/identity230c/2201SAproject
	- github 링크