# MAPD-B

Lectures for the Management and Analysis of Physics Datasets (Module B) course - MSc in Physics of Data - University of Padova - Academic year 2022-2023.

## Docker

All exercises are run using Docker.

In this way, the only thing you need to install is docker itself (instructions for Mac, Windows and linux can be found [here](https://docs.docker.com/get-docker/)).

For this exercise, we will use docker-compose to simulate a cluster with a number of nodes: 
- 1 container running the Spark `master` (the head-node of the cluster) with the Cluster Resource Manager
- 1 _or more_ containers running Spark `workers` (the processing-nodes of the cluster)
- 1 container running the Spark client, the Python interpreter and a Jupyter-notebook server
- 1 _or more_ containers acting each as a Kafka broker we want to create
- 1 additional container running the Zookeper service that will be used by the Kafka cluster to store the offsets of the messages (metadata)

This is once again an "overkill" setup that can however be useful to understand and test a container-based complex environment with multiple active services. The client-jupyter container is in fact superfluos, as you could use your local machine to run these services, after installing all libraries and modules required to run the Spark client.

Have a look at the `docker-compose.yml` file to see how the system is set up.

## Docker compose

All services of the cluster can be spawned with 

```
docker compose up
```

By default, only one worker is created, with 1 core and 512 MB of memory.

If you want to use an arbitrary number **N** of workers, you can scale the cluster with:

```
docker compose up --scale spark-worker=N
```

Additionally, only one broker is created.

If you want to use an arbitrary number **M** of brokers, you can scale the cluster with:

```
docker compose up --scale kafka-broker=M
```

You can further combine the two by scaling independently both the Spark workers and the Kafka brokers, e.g.:

```
docker compose up --scale spark-worker=N --scale kafka-broker=M
```

It is however strongly suggested to start a cluster with at least 2 `spark-workers` and exactly 1 `kafka-broker`:

```
docker compose up --scale spark-worker=2 --scale kafka-broker=1
```

After the cluster has been created you can navigate to `localhost:1234` to access the Jupyter service from your browser. 

The Spark `master` service has already been created, and a port mapping has been enabled to ensure you can reach its dashboard from outside the container. 

The Spark cluster dashboard will be available on `localhost:8080`, and the Spark application dashboard will be available on `localhost:4040`.

As always, the cluster of running containers can be shut down by typing
```
docker compose down
```

## Lecture

* Create and inspect topics from shell
* Console-based Producer and Consumer
* Pythonic APIs for Producer and Consumer (based on `kafka-python`)
* Consumer groups
* Spark Structured Streaming ingesting data from Kafka