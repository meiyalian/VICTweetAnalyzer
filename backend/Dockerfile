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

FROM base
WORKDIR /usr/backend

#ENV PORT "5000"
COPY . .

RUN pip install -r requirements.txt

# install dependency to conda
# RUN npm install -g electron@1.8.4 orca \
#     && pip install psutil requests

ENV flask_port 80
ENV flask_host 0.0.0.0

EXPOSE $flask_port
#RUN ./run_flask_debug_mode.sh
# ENTRYPOINT ["sh", "-c"]
CMD ["python3 app.py -host $flask_host -port $flask_port"]