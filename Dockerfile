FROM python:3.10-slim-buster

WORKDIR /flask-app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# changing the directory for initialization of db
WORKDIR /flask-app/Blueprints

RUN flask db init
RUN flask db migrate
RUN flask db upgrade

# back to our root directory
WORKDIR /flask-app

CMD ["python3", "run.py"]