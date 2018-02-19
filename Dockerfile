FROM python:3-slim
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
