FROM base-image

EXPOSE ${ZOOKEEPER_PORT} 2181

CMD ${KAFKA_HOME}/bin/zookeeper-server-start.sh ${KAFKA_HOME}/config/zookeeper.properties #>> /dev/null
