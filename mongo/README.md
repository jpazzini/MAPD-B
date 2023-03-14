# MAPD-B

Lectures for the Management and Analysis of Physics Datasets (Module B) course - MSc in Physics of Data - University of Padova - Academic year 2022-2023.

## Docker

All exercises are run using Docker.

In this way, the only thing you need to install is docker itself (instructions for Mac, Windows and linux can be found [here](https://docs.docker.com/get-docker/)).

For this exercise, we will use docker-compose to simulate a system with 2 nodes: 
- 1 MongoDB server (acting as a "remote" database server). A single-server setup is instantiated in this case, although a replica-set or a sharded set of replica-sets could be used.
- 1 service running the MongoDB client, the Python interpreter and a Jupyter-notebook

This is an "overkill" setup that can however be useful to understand and test a container-based environment with multiple active services.
The client-jupyter container is in fact superfluos, as you could use your local machine to run these services, after installing all libraries and modules required to run the MongoDB client. 

Check the `docker-compose.yml` file to see how the system is set up.

- The MongoDB container will be downloaded from one official MongoDB image on dockerhub
- The Jupyter-notebook container image should be already built from the `mapd_notebook.dockerfile` Docker-file contained in `MAPD-B/mysql/docker/`

## Docker compose

All services can be spawned with 

```
docker compose up
```

Using the port forwarding from the docker-compose yml, we expose the Jupyter-notebook service on the port 1234 (you can change the port if you prefer).

By pointing a browser to `localhost:1234` you will see a Jupyter service running.

Remember that this is however running *inside a container* and not directly in your local machine...

The other running service is a MongoDB server.

The two-nodes cluster can be shut down by typing

```
docker compose down
```

## Pre-requisites

1. Clone this repo (or fetch the latest updates) 
2. Verify to you have already built the `mapd_notebook` Docker image using `docker image ls`
  - if not, you should build it with `mapd_notebook` as the image tag 
3. Test that the `docker compose` can be started (`up`) and stopped (`down`) succesfully 
4. Download the `YELP.json` file (~110 MB) at the link you can find on Moodle and move it under the `MAPD-B/mongo/dbs/` path
