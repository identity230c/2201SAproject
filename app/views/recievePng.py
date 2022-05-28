from fileinput import filename
from flask import Blueprint, render_template, url_for, request, current_app
import os 
from .models import sendRequest
bp = Blueprint('main', __name__, url_prefix='/testImg', template_folder='templates')


  
@bp.route('/')
def index():
  return render_template('uploadImg.html')

@bp.route('/upload', methods=['GET','POST'])
def upload():
  if request.method == 'POST':
    if 'file' not in request.files:
      return "아니 이게 왜 안되냐고"
    f = request.files['file']
    if f.filename == '':
      return "업로드가 안된거 같은데"
    else: 
      testSrc = './app/static/images/testImg.png'#os.path.join(current_app.config['IMG_FOLDER'], 'testImg.png')
      f.save(testSrc)
      ans = sendRequest(testSrc, current_app.config['tfServer'])
      print(ans)
      return render_template('testImg.html', imgSrc = 'testImg.png', ans=ans)

  