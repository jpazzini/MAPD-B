FROM base-image

CMD ${KAFKA_HOME}/bin/kafka-server-start.sh ${KAFKA_HOME}/config/server.properties --override zookeeper.connect=${ZOOKEEPER_HOST}:2181  #>> /dev/null
