# MAPD-B

Lectures for Management and Analysis of Physics Datasets course MSc in Physic of Data at University of Padua 2021-2022.

## Docker

All exercises are run using Docker.

In this way, the only thing you need to install is docker itself (instructions for Mac, Windows and linux can be found [here](https://docs.docker.com/get-docker/)).

For this exercise, we will use docker-compose to simulate a system with 2 nodes: 1 MongoDB server, and 1 server running a Jupyter-notebook service.

This is an "overkill" setup that can however be useful to understand and test a container-based environment with multiple active services.

Check the `docker-compose.yml` file to see how the system is set up.

- The MongoDB container will be downloaded from one official MongoDB image on dockerhub
- The Jupyter-notebook container image built from the `mapd_notebook.dockerfile` Docker-file contained in `MAPD-B/mysql/docker/`

## Docker compose

All services can be spawned with 

```
docker-compose up
```

Using the port forwarding from the docker-compose yml, we expose the Jupyter-notebook service on the port 8888 (you can change the port if you prefer).

By pointing a browser to `localhost:8888` you will see a Jupyter service running.

Remember that this is however running *inside a container* and not directly in your local machine...

The other running service is a MongoDB server.

The two-nodes cluster can be shut down by typing

```
docker-compose down
```

## Pre-requisites

1. Clone this repo (or check for updates) 
2. Verify to you have already built the `mapd_notebook` Docker image using `docker image ls`
  - if not, you should build it with `mapd_notebook` as the image tag 
3. Test that the `docker-compose` can be started (`up`) and stopped (`down`) succesfully 
4. Download the `YELP.json` file at the link you can find on the course moodle (~110 MB) and place it under the `MAPD-B/mongo/dbs/` path
