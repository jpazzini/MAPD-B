FROM continuumio/miniconda3:4.9.2

ARG shared_workspace=/opt/workspace
ENV SHARED_WORKSPACE=${shared_workspace}

# -- Layer: java
RUN mkdir -p /usr/share/man/man1
RUN apt-get -y update && \
    apt-get install --no-install-recommends -y \
    "openjdk-11-jre-headless" \
    ca-certificates-java && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# -- Layer: kafka
ARG kafka_version=2.7.0
ARG scala_version=2.13

RUN apt-get update -y && \
    apt-get install -y curl && \
    apt-get install -y tmux && \
    curl https://archive.apache.org/dist/kafka/${kafka_version}/kafka_${scala_version}-${kafka_version}.tgz -o kafka.tgz && \
    tar -xf kafka.tgz && \
    mv kafka_${scala_version}-${kafka_version} /usr/bin/ && \
    mkdir /usr/bin/kafka_${scala_version}-${kafka_version}/logs && \
    rm kafka.tgz

ENV ZOOKEEPER_PORT 2181
ENV ZOOKEEPER_HOST zookeeper
ENV KAFKA_HOME /usr/bin/kafka_${scala_version}-${kafka_version}

# -- Install kafka-python
RUN conda install -y -c conda-forge kafka-python

# -- Install proc tools
RUN apt-get update && apt-get install -y procps && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

SHELL ["/bin/bash", "-c"]
