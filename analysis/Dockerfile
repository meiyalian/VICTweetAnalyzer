FROM python:3.5.0

# there lines are dedicate for nectar server
ENV http_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV HTTP_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV HTTPS_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV no_proxy localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.u nimelb.edu.au,.cloud.unimelb.edu.au

COPY . /app/analysis 
WORKDIR /app/analysis
RUN pip3 install torch==1.0.1 -f https://download.pytorch.org/whl/cpu/stable 
RUN sudo git clone https://github.com/huggingface/torchMoji
RUN import os 
RUN os.chdir('torchMoji')
RUN pip3 install -e
CMD ["python3", "-u","sentiment.py"]