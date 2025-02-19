FROM python:3.13.2-slim

WORKDIR /mapd-workspace

ENV PIP_DEFAULT_TIMEOUT=100 \
   PYTHONUNBUFFERED=1 \
   PIP_DISABLE_PIP_VERSION_CHECK=1 \
   PIP_NO_CACHE_DIR=1

RUN pip install notebook \
               matplotlib \
               SQLAlchemy==2.0.38 \
               ipython-sql==0.5.0 \
               mysql-connector-python==9.2.0 \
               pandas


EXPOSE 8888

CMD jupyter notebook \
   --ip=0.0.0.0 \
   --port=8888 \
   --no-browser \
   --allow-root \
   --NotebookApp.token=
