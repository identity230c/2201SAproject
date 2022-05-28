import json
import requests
import numpy as np
import tensorflow as tf

def sendRequest(filename, address):
  raw = tf.io.read_file(filename)
  img = tf.image.decode_png(raw, channels=1)
  img = np.expand_dims(img.numpy().squeeze(), axis=[0,-1])
  
  data = json.dumps({
    'instances' : img.tolist()
  })
  resp = requests.post(address, data=data)
  
  ans = json.loads(str(resp.content, 'utf-8'))['predictions']
  return np.argmax(ans)