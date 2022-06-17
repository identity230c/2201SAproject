from flask import Flask, render_template

from app.controls import Canvas

def create_app():
  app = Flask(__name__, template_folder='views')  

  app.config['IMG_FOLDER'] = './app/static/images/'
  app.config['tfServer'] = 'http://tf_server:8501/v1/models/test:predict'

  from app.controls import UploadImg, Canvas
  
  app.register_blueprint(Canvas.bp)
  app.register_blueprint(UploadImg.bp)
  
  @app.route('/')
  def index():
    return render_template('index.html')
  
  return app

