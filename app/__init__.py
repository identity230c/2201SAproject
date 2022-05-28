from flask import Flask
import os

def create_app():
  app = Flask(__name__, template_folder='templates')

  app.config['IMG_FOLDER'] = os.path.join('./static','images')
  app.config['tfServer'] = 'http://host.docker.internal:8501/v1/models/test:predict'

  from app.views import recievePng # 블루프린트가 있는 패키지명, 파일명 순
  app.register_blueprint(recievePng.bp)

  @app.route('/')
  def index():
    return '인덱스임'

  return app
