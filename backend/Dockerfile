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
CMD ["python backend.py -host $flask_host -port $flask_port"]