FROM iron/python:2.7
MAINTAINER Franciscon Santos - francisconp@gmail.com
RUN apk update
RUN apk add py-pip gcc python-dev musl-dev libffi-dev openssl-dev
RUN rm -rf /var/cache/apk/*
RUN mkdir /app
COPY requirements.txt /app/requirements.txt
COPY twitter_data_mining.py /app/twitter_data_mining.py
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
ENTRYPOINT python /app/twitter_data_mining.py
