FROM python:3-alpine
ADD . /code
WORKDIR /code
RUN apk add --no-cache bash && pip install -r requirements.txt
