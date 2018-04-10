FROM python:3

RUN mkdir -p /usr/chal

WORKDIR /usr/chal

ADD ./results.txt .
ADD ./service.py .


EXPOSE 12345

CMD [ "python3", "/usr/chal/service.py" ]
