# MAPD-B

Lectures for Management and Analysis of Physics Datasets course MSc in Physic of Data at University of Padua 2021-2022.

## Docker

It is possible to run all the exercises using docker. 

In this way, the only thing you need to install is docker itself (instructions for Mac, Windows and linux can be found [here](https://docs.docker.com/get-docker/)).

Clone this repo if has not already been done.

For this exercise, we will use docker-compose to simulate a system with 2 nodes: 1 MySQL server, and 1 server running a Jupyter-notebook service.

This is an "overkill" setup that can however be useful to understand and test a container-based environment with multiple active services.

Check the `docker-compose.yml` file to see how the system is set up.

### Docker compose

All services can be spawned with 

```
docker-compose up
```

Using the port forwarding from the docker-compose yml, we expose the Jupyter-notebook service on the port 8888 (you can change the port if you prefer).

By pointing a browser to `localhost:8888` you will see a Jupyter service running.

Remember that this is however running *inside a container* and not directly in your local machine...

The other running service is a MySQL server.

The two-nodes cluster can be shut down by typing

```
docker-compose down
```
