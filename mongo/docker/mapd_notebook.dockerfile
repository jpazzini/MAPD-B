FROM continuumio/miniconda3:4.10.3p1

ARG shared_workspace=/opt/workspace
ENV SHARED_WORKSPACE=${shared_workspace}

RUN apt-get update -y && \
    pip3 install notebook matplotlib ipython-sql pymysql mysql-connector-python pandas pymongo

EXPOSE 8888

CMD jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.iopub_data_rate_limit=1.0e10 --NotebookApp.token= 


