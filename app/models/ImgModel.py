import base64
from PIL import Image
from io import BytesIO

class ImgOperation: # 추상클래스
  def __init__(self, raw, path, filename, format="png"):
    self.cooked = self.cooking(raw)
    self.path = path 
    self.filename = filename
    self.format = format
    self.saveOrigin()
    self.saveSmall()

  def cooking(self, raw):
    # 추상 메서드
    return 
  
  def saveOrigin(self):
    # 추상 메서드
    return 
  
  def saveSmall(self):
    raw = Image.open(self.getOriginPath())
    cooked = raw.resize((28, 28))
    cooked.save(self.getSmallPath(), self.format)

  def getOriginPath(self):
    return self.path + self.getFileName()

  def getSmallPath(self):
    return self.path + self.filename+"-small" + "." + self.format 
  
  def getFileName(self):
    return self.filename + '.' + self.format
      

class Base64ToPng(ImgOperation):  
  # Base64로 들어온 request를 png로 변환하는 subclass
  
  def cooking(self, raw):
    return Image.open(BytesIO(base64.b64decode(raw)))
  
  def saveOrigin(self):
    self.cooked.save(self.getOriginPath(), self.format)


class FormDataToPng(ImgOperation):
  # form data로 전달된 img file을 png로 변환하는 subclass
  
  def cooking(self, raw):
    return raw
  
  def saveOrigin(self):
    self.cooked.save(self.getOriginPath())