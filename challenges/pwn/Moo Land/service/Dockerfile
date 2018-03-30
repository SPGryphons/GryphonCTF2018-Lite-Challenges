FROM ubuntu:latest

ENV HOME=/home/moo

RUN apt-get update && \
    apt-get install -y nodejs cowsay

RUN useradd -s /bin/rbash -m moo

COPY ./banner.txt /home/moo/
COPY ./server.js /home/moo/
COPY ./flag.txt /home/moo/

WORKDIR /home/moo

RUN mkdir progs && \
    ln -s /bin/ls progs/ && \
    ln -s /bin/cat progs/ && \
    ln -s /usr/games/cowsay progs/

RUN chown -R root:moo /home/moo && \
    chmod -R 750 /home/moo

USER moo
ENV PATH=/home/moo/progs
EXPOSE 5000

CMD ["/usr/bin/nodejs", "/home/moo/server.js"]
