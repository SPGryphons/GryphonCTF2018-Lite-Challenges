FROM ubuntu:latest

ENV HOME=/home/moo

RUN apt-get update
RUN apt-get install -y nodejs cowsay

RUN useradd -m moo

COPY ./banner.txt /home/moo/
COPY ./server.js /home/moo/
COPY ./flag.txt /home/moo/

RUN chown -R root:moo /home/moo
RUN chmod -R 750 /home/moo

USER moo
WORKDIR /home/moo

EXPOSE 5000

CMD ["nodejs", "/home/moo/server.js"]
