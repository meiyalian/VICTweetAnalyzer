FROM ubuntu:18.04 AS base
RUN set -xe \
    && apt-get update \
    && apt-get install python-pip
RUN pip install --upgrade pip

FROM base
WORKDIR /usr/backend

#ENV PORT "5000"
COPY . .

RUN pip install -r requirements.txt

# install dependency to conda
# RUN npm install -g electron@1.8.4 orca \
#     && pip install psutil requests

ENV flask_port 5000
ENV flask_host 0.0.0.0

EXPOSE $flask_port
#RUN ./run_flask_debug_mode.sh
# ENTRYPOINT ["sh", "-c"]
CMD ["python3 app.py -host $flask_host -port $flask_port"]