FROM python:3.8.5

# there lines are dedicate for nectar server
ENV http_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV HTTP_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV HTTPS_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV no_proxy localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.u nimelb.edu.au,.cloud.unimelb.edu.au

COPY . /app/crawler
WORKDIR /app/crawler
RUN pip install -r requirements.txt
RUN pip3 install --user --upgrade -e git+https://github.com/twintproject/twint.git@origin/master#egg=twint
CMD ["python3", "-u","GetOldTweets.py"]