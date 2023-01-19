FROM python:3.10.0
WORKDIR /monitoring-service
COPY . /monitoring-service
RUN pip3 install -r requirements.txt
EXPOSE 8000
RUN chmod 755  docker-entrypoint.sh
ENV PYTHONPATH /monitoring-service
ENTRYPOINT ["./docker-entrypoint.sh"]