# MAPD-B

Lectures for Management and Analysis of Physics Datasets course MSc in Physic of Data at University of Padua 2021-2022.

## Docker

All exercises can be run using Docker.

In this way, the only thing you need to install is docker itself (instructions for Mac, Windows and linux can be found [here](https://docs.docker.com/get-docker/)).

You can choose to run it in **two ways**: 
1. Using a _single container_, simulating the set up for a "local cluster"
2. Using `docker-compose` to simulate the behaviour of a real N-machine cluster, where master and workers will be on different nodes

### 1. Single container

Run the following command, from inside `MAPD-B/dask` directory, to create a container with Dask and Jupyter already installed.
The first time you run it may take a while because it needs to download all the necessary components and libraries from DockerHub.
However, the next times you will need this container it will be created instantly since all the components are cached.

You will need to open up and forward the ports 8787, 8888, 8786.
You will also need to mount as a volume the local folder onto the container path `/opt/workspace`.

```
docker run --rm -it \
        -p 8888:8888 \
        -p 8787:8787 \
        -v $PWD:/opt/workspace \
        jpazzini/mapd-b:dask-client-jupyter
```

Once it has been created, you can connect to Jupyter from your local browser by typing `localhost:8888`. 
Make sure that other Jupyter-Notebooks are not already using this port. 


### 2. Docker cluster

We can simulate multiple nodes by using multiple Docker containers.

Have a look at the `docker-compose.yml` file to see how the system is set up.

- A container hosting the Jupyter-Notebook server, acting as the client from which we will deploy applications to the Dask cluster 
- A container running as the Dask Scheduler with the Cluster Resource Manager
- A number of additional containers, one per each Dask worker we want to create


This cluster can be spawned with 

```
docker-compose up
```

By default, only one worker is created, each worker with 1 core and 512 MB of memory.
If you want to use an arbitrary number **N** of workers, you can scale the cluster with:

```
docker-compose up --scale dask-worker=N
```

Again, after the cluster has been created you can navigate to `localhost:8888` to open the Jupyter dashboard. 

In this case the Dask Scheduler has already been created, you don't need to start it manually. 
Indeed the Dask cluster dashboard will be already available on `localhost:8787`. 

If you want to use more resources per each worker, edit the file `docker-compose.yml` and change `DASK_WORKER_CORES`, `DASK_WORKER_THREADS` and `DASK_WORKER_MEMORY` to the value you prefer. 

The cluster can be shut down by typing
```
docker-compose down
```

## Local cluster

As an alternative, you can install and use Dask directly from your local machine, or from a virtual machine you may have created.

Dask can be installed with `pip3 install dask[complete]` or `conda install dask[complete]`.

Please note that in this case, the teacher and the teaching assistants will not provide any support for your private installations and the possible missing modules and dependencies, that you will have to install on your own.

It is therefore strongly suggested to use either the Docker Cluster or Single Docker Container deployment of Dask to run the hands-on sessions.

## Lecture 1

* Creation of a Dask cluster
* Basic commands (eager and lazy execution)
* Dask application WebUI

