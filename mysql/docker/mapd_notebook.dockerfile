FROM continuumio/miniconda3:4.12.0

WORKDIR /mapd-workspace

RUN conda install -y psutil

RUN pip3 install notebook \
                 matplotlib \
                 SQLAlchemy==1.4.46 \
                 ipython-sql==0.4.1 \
                 mysql-connector-python \
                 pandas \
                 pymongo

RUN apt-get clean
RUN conda clean -y -a
RUN pip3 cache purge

EXPOSE 8888

CMD jupyter notebook \
    --ip=0.0.0.0 \
    --port=8888 \
    --no-browser \
    --allow-root \
    --NotebookApp.token= 
