# MAPD-B

Lectures for Management and Analysis of Physics Datasets course MSc in Physic of Data at University of Padua 2021-2022.

## Docker

It is possible to run all the exercises using docker. This is particularly usefull if you are experiencing problems with VirtualBox or you don't want to go to the trouble of setting up the environment. 

In this way, the only thing you need to install is docker itself (instructions for Mac, Windows and linux can be found [here](https://docs.docker.com/get-docker/)).

Using docker-compose to simulate the behaviour of a Spark cluster, where master and workers will be on different nodes, and an independent Kafka broker.

Clone this repo if has not already been done.

### Docker cluster

We can simulate multiple nodes by using multiple docker containers: a container hosting jupyter server and acting as the client node of the cluster, a container with the resource manager and one container for each worker, plus a hosting a kafka broker. In this case you can think each container as a *virtual machine*. This setup is simulating what you experience on a real cluster. 

This cluster can be spawned with 

```
docker-compose up
```

By default, only one worker and one broker are created. If you want to use N workers you can scale the cluster with

```
docker-compose up --scale spark-worker=N
```

and if you want to use M kafka brokers you can do it with:

```
docker-compose up --scale kafka-broker=M
```

After the cluster has been created you can navigate to `localhost:8888` to open the Jupyter dashboard. 
The Spark master has already been created, you don't need to start it manually. 
Zookeeper and the Kafka server has also already been started automatically. 

The Spark cluster dashboard will be already available on `localhost:8080`.

If you want to use more resources per each worker, edit the file `docker-compose.yml` and change `SPARK_WORKER_CORES` and `SPARK_WORKER_MEMORY`
to the value you prefer. 

The cluster can be shut down either by pressing `ctrl+C` or by typing
```
docker-compose down
```

In case you have stopped it by pressing `ctrl+C` remove the containers and network with `docker-compose rm -f`.
