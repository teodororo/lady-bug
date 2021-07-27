FROM python:3.7-slim

#RUN apt update -y && apt upgrade -y

ADD . /app
WORKDIR /app

RUN export $(cat .env | xargs)

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python", "server.py"]