#!/bin/bash

KAFKA='kafka_2.11-0.10.1.1'

/app/$KAFKA/bin/zookeeper-server-start.sh \
-daemon /app/$KAFKA/config/zookeeper.properties

sleep 30

/app/$KAFKA/bin/kafka-server-start.sh /app/$KAFKA/config/server.properties
