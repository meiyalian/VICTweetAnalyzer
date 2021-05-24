# FROM node:14.3.0

# ENV http_proxy http://wwwproxy.unimelb.edu.au:8000/
# ENV https_proxy http://wwwproxy.unimelb.edu.au:8000/
# ENV HTTP_PROXY http://wwwproxy.unimelb.edu.au:8000/
# ENV HTTPS_PROXY http://wwwproxy.unimelb.edu.au:8000/
# ENV no_proxy localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.u nimelb.edu.au,.cloud.unimelb.edu.au

# EXPOSE 80
# COPY . /app/fronend
# WORKDIR /app/fronend

# RUN npm install -g @vue/cli
# ENTRYPOINT ["npm", "run"]
FROM node:lts-alpine
ENV http_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV HTTP_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV HTTPS_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV no_proxy localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.u nimelb.edu.au,.cloud.unimelb.edu.au
COPY . /app/frontend
WORKDIR /app/frontend
COPY package*.json ./
RUN npm install
EXPOSE 8080
# start app
CMD ["npm", "start"]