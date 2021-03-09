FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine

COPY ./app /app

RUN pip3 install --no-cache --upgrade -r requirements.txt
