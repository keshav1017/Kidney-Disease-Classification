FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y

WORKDIR /app

COPY flask_app/ /app/

COPY models/model.h5 /app/models/model.h5

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]