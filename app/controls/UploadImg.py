from flask import Blueprint, render_template, request, current_app
from app.models import ImgModel, TfModel

bp = Blueprint('uploadImg', __name__, url_prefix='/upload', template_folder='views')

# 사용자가 업로드한 이미지 질의하는 파일
@bp.route('/')
def upload():
  return render_template('uploadPage.html')

@bp.route('predict', methods=["POST"])
def uploadPredict():
  try:
    if request.method == "POST":
      filename = 'uploadImg'
      model1 = ImgModel.FormDataToPng(request.files['file'], current_app.config['IMG_FOLDER'], filename)
      model2 = TfModel.TfModel(current_app.config['tfServer'], model1.getSmallPath())
      return render_template('resultPage.html', imgSrc = model1.getFileName(), ans=model2.getAns())
    else:
      return render_template('errInfo.html', errHead='잘못된 접근', errBody='잘못된 접근입니다. 이 페이지는 GET 접근을 허용하지 않습니다. upload페이지를 통해 접근하십시오')
  except Exception as e:
    return render_template('errInfo.html', errHead='서버오류', errBody='서버에서 오류가 발생하였습니다. 오류메시지 : ' + str(e))