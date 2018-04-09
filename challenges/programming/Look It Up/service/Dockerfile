FROM python:3-alpine
RUN mkdir -p /opt/chal
COPY ./* /opt/chal/
WORKDIR /opt/chal
CMD ["python3", "/opt/chal/server.py"]
