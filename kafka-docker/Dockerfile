FROM ubuntu:latest

RUN mkdir /Kafka
# COPY /Users/etlaou/Downloads/Kafka/confluent-6.1.0 /Kafka/
COPY . /Kafka/
# COPY /Users/etlaou/Downloads/Kafka/confluentinc-kafka-connect-jdbc-10.1.0 /Kafka

ENTRYPOINT /confluent-6.1.0/bin/kafka-server-start.sh config/server.propertiesㅌ