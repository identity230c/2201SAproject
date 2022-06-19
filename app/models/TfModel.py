import numpy as np
from PIL import Image
import json
import requests

class TfModel:
  # tensorflow server와 http 통신하는 객체
  def __init__(self, server,path):
    self.readPng(path)
    self.server = server
    self.sendRequest()    

  def readPng(self, path):
    # tensorflow server에서 사용할 수 있도록 이미지 마셜링
    self.png = Image.open(path).convert('L')
    self.png = np.array(self.png)
    self.png = np.expand_dims(self.png, axis=[0,-1])

  def sendRequest(self):
    # 통신
    data = json.dumps({
      'instances' : self.png.tolist()
    })
    resp = requests.post(self.server, data=data)
    self.ans = json.loads(str(resp.content, 'utf-8'))['predictions']
    self.ans = np.argmax(self.ans)
  
  def getAns(self):
    # 질의 결과 반환
    return self.ans