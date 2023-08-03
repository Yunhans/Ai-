FROM python:3.8.15

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

CMD [ "python" , "app.py" ]