FROM python:3.6.9

# there lines are dedicate for nectar server
ENV http_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV HTTP_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV HTTPS_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV no_proxy localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.u nimelb.edu.au,.cloud.unimelb.edu.au

COPY . /app/analysis 
WORKDIR /app/analysis
RUN pip install --upgrade pip
RUN python3 -m pip install torch==1.0.1 -f https://download.pytorch.org/whl/cpu/stable 
RUN python3 -m pip install -e .
RUN python3 -m pip install -r requirements.txt
WORKDIR /app/analysis
RUN pip install .
RUN echo 'y' | python scripts/download_weights.py

CMD ["python3", "-u","sentiment.py"]
