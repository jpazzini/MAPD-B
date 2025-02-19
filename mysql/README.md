## SQL module

### Docker

All exercises are to be run using Docker.

In this way, the only thing you need to install is `docker` itself (instructions for Mac, Windows and Linux can be found [here](https://docs.docker.com/get-docker/)).

For this exercise, we will use `docker compose` to simulate a system with 2 nodes: 
- 1 **MySQL server** (acting as a "remote" database server running a RDBMS)
- 1 service running the **MySQL client, the Python interpreter and a Jupyter-notebook**

While this setup may seem excessive, it can be useful to understand and test a container-based environment with multiple active services.
The client-jupyter container is, in fact, superfluous, as you could use your local machine to run these services, after installing all libraries and modules required to run the MySQL client. 


Refer to the `docker-compose.yml` file for details on the system setup.

- The MySQL container will be downloaded from an official MySQL image on Docker Hub
- The Jupyter-notebook container image has to be built from the `mapd_notebook.dockerfile` Docker-file contained in `MAPD-B/mysql/docker/`


### Docker compose

All services can be spawned with 

```
docker compose up
```

Using the port forwarding from the docker-compose yml, we expose the Jupyter-notebook service on the port 1234 (you can change the port, if you so prefer).

By pointing your browser to `localhost:1234` you will see a Jupyter service running.

Remember that this notebook is however running ***inside a container*** and not directly in your local machine...

The other running service is a MySQL server.

### Shutting down the Docker compose "cluster"

The two services can be stopped with an interrupt from the terminal (`CTRL+c`), or issuing the stop of the containers from a second terminal.

The two-nodes cluster can be finally shut down by typing

```
docker compose down
```

### Pre-requisites

1. Clone this repo (or fetch the latest updates) 
2. Build the `mapd_notebook` Docker image using `mapd_notebook` as the image tag (see the Docker slides for instructions)
3. Test that the `docker compose` can be started (`up`) and stopped (`down`) succesfully 
4. Download the `IMDb_pruned.sql` file (~350 MB) at the link you can find on Moodle and move it under the `MAPD-B/mysql/dbs/` path
