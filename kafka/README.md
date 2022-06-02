# MAPD-B

Lectures for Management and Analysis of Physics Datasets course MSc in Physic of Data at University of Padua 2021-2022.

## Docker

It is possible to run all the exercises using docker.  

In this way, the only thing you need to install is docker itself (instructions for Mac, Windows and linux can be found [here](https://docs.docker.com/get-docker/)).

No single-docker container deployment will be provided in this repository.

Instead, we will use docker-compose to simulate the behaviour of a Spark cluster, where master and workers will be on different nodes, and an independent Kafka broker.

Clone this repo if has not already been done.

### Docker cluster

We can simulate multiple nodes by using multiple Docker containers.

Have a look at the `docker-compose.yml` file to see how the system is set up.

- A container hosting the Jupyter-Notebook server, acting as the client from which we will deploy applications to the Spark cluster, and to interact with the Kafka cluster 
- A container running as the Spark Master with the Cluster Resource Manager
- A number of additional containers, one per each Spark worker we want to create
- One or more containers, one per each Kafka broker we want to create
- An additional container running the Zookeper application that will be used by the Kafka cluster to store the offsets of the messages

This cluster can be spawned with 

```
docker-compose up
```

By default, only one worker and one broker are created. If you want to use **N** Spark workers you can scale the cluster with

```
docker-compose up --scale spark-worker=N
```

and if you want to use **M** kafka brokers you can do it with:

```
docker-compose up --scale kafka-broker=M
```

A combination of the two is possible, for example:

```
docker-compose up --scale spark-worker=3 --scale kafka-broker=2
```

A suggestion is to use 2 Spark workers and 1 Kafka broker, i.e.:
    
```
docker-compose up --scale spark-worker=2 --scale kafka-broker=1
```

After the cluster has been created you can navigate to `localhost:8888` to open the Jupyter dashboard. 

The Spark master has already been created, you don't need to start it manually. 
Zookeeper and the Kafka server has also already been started automatically. 

The Spark cluster dashboard will be already available on `localhost:8080`.

If you want to use more resources per each worker, edit the file `docker-compose.yml` and change `SPARK_WORKER_CORES` and `SPARK_WORKER_MEMORY`
to the value you prefer. 

The cluster can be shut down by pressing `ctrl+C` followed by
```
docker-compose down
```

In case you have only stopped it by pressing `ctrl+C`, we suggest you to remove the dangling containers and network with `docker-compose rm -f`.

## Local cluster

As an alternative, you can install and use Spark and Kafka directly from your local machine, or from a virtual machine you may have created.

The Spark binaries can be downloaded from the [link](https://spark.apache.org/downloads.html).
Please read carefully the instructions provided in the dedicated [page](https://spark.apache.org/docs/latest/).
To run locally, Spark also requires to have Java (version 8 or version 11) installed in your system.

The Kafka binaries can be downloaded from the [link](https://kafka.apache.org/downloads.html).
Kafka will rely on the same Java version as Spark.
A useful quick start guide can be found [here](https://kafka.apache.org/quickstart).
Please also read the [documentation](https://kafka.apache.org/documentation.html) for more information.

Please note that in this case, the teacher and the teaching assistants will not provide any support for your private installations.

It is therefore strongly suggested to use either the Docker Cluster deployment of Spark to run the hands-on sessions.
