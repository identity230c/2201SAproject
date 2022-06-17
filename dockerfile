FROM continuumio/miniconda3

WORKDIR /saProject

RUN pip install flask
RUN pip install numpy
RUN pip install pillow

COPY ./app ./app

ENV FLASK_APP app 
ENV FLASK_ENV development

RUN set FLASK_APP=$FLASK_APP
RUN set FLASK_ENV=$FLASK_ENV

EXPOSE 8080

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]

