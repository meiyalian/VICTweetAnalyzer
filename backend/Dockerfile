FROM ubuntu:18.04 AS base
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
# ENV PATH /opt/conda/bin:$PATH
ENV http_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV HTTP_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV HTTPS_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV no_proxy localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.u nimelb.edu.au,.cloud.unimelb.edu.au

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# https://hub.docker.com/r/library/python/tags/
# FROM python:3-onbuild
FROM python:alpine3.7
# Coping source in current directory into the image
# python:3-onbuild expects the source in /usr/src/app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]

# # Commands in a list
# CMD ["python", ".py"]

# #ENV PORT "5000"
# COPY . .
# WORKDIR /code
# RUN pip install -r requirements.txt

# install dependency to conda
# RUN npm install -g electron@1.8.4 orca \
#     && pip install psutil requests

# ENV flask_port 80
# ENV flask_host 0.0.0.0

# EXPOSE $flask_port
#RUN ./run_flask_debug_mode.sh
# ENTRYPOINT ["sh", "-c"]
# CMD ["python","app.py"]