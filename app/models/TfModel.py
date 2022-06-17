import numpy as np
from PIL import Image
import json
import requests

class TfModel:
  def __init__(self, server,path):
    self.readPng(path)
    self.server = server
    self.sendRequest()    

  def readPng(self, path):
    self.png = Image.open(path).convert('L')
    self.png = np.array(self.png)
    self.png = np.expand_dims(self.png, axis=[0,-1])

  def sendRequest(self):
    req = data = json.dumps({
      'instances' : self.png.tolist()
    })
    resp = requests.post(self.server, data=data)
    self.ans = json.loads(str(resp.content, 'utf-8'))['predictions']
    self.ans = np.argmax(self.ans)
  
  def getAns(self):
    return self.ans