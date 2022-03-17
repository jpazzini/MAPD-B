docker build \
 -f base-image.Dockerfile \
 -t base-image .

docker build \
 -f zookeeper.Dockerfile \
 -t zookeeper .

docker build \
 -f kafka-broker.Dockerfile \
 -t kafka-broker .

