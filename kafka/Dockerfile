FROM iron/java
MAINTAINER Franciscon Santos - francisconp@gmail.com
RUN apk update
RUN apk add bash
RUN apk add procps
RUN rm -rf /var/cache/apk/*
RUN mkdir /app
WORKDIR /app
RUN wget -qO- http://mirror.nbtelecom.com.br/apache/kafka/0.10.1.1/kafka_2.11-0.10.1.1.tgz | tar -zxf -
COPY start_kafka.bash .
ENTRYPOINT /bin/bash start_kafka.bash
