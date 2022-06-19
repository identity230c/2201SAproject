from flask import Blueprint, render_template, url_for, request, current_app
from app.models import ImgModel, TfModel

bp = Blueprint('canvas', __name__, url_prefix='/canvas', template_folder='views')

# Canvas로 사용자가 그린 그림 질의하는 파일
@bp.route('/')
def canvas():
  return render_template('canvasPage.html')

@bp.route('/predict', methods=["GET","POST"])
def canvasPredict():
  try:
    if request.method == "POST":
      raw = request.form["file"].split(',')[-1]
      filename = 'canvasImg'
      model1 = ImgModel.Base64ToPng(raw,current_app.config['IMG_FOLDER'],filename)
      model2 = TfModel.TfModel(current_app.config['tfServer'], model1.getSmallPath())
      return render_template('resultPage.html', imgSrc=model1.getFileName(), ans=model2.getAns())
    else:
      return render_template('errInfo.html', errHead='잘못된 접근', errBody='잘못된 접근입니다. 이 페이지는 GET 접근을 허용하지 않습니다. canvas페이지를 통해 접근하십시오')
  except Exception as e:
    return render_template('errInfo.html', errHead='서버오류', errBody='서버에서 오류가 발생하였습니다. 오류메시지 : ' + str(e))