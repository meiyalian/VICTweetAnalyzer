FROM python:3.7.0

# there lines are dedicate for nectar server
ENV http_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV HTTP_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV HTTPS_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV no_proxy localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.u nimelb.edu.au,.cloud.unimelb.edu.au

COPY . /app/analysis 
WORKDIR /app/analysis
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip3 install torch torchvision scipy
WORKDIR /app/analysis/torchMoji
RUN python setup.py install
RUN python scripts/download_weights.py
# RUN pip install emoji numpy scipy scikit-learn text-unidecode
WORKDIR /app/analysis
CMD ["python3", "-u","sentiment.py"]