FROM ubuntu:latest

RUN useradd -s /usr/sbin/nologin -m magician
RUN apt-get update && apt-get install -y xinetd

COPY ./magician /home/magician/
COPY ./exec.sh /home/magician/
COPY ./magicianService /etc/xinetd.d/

RUN chown -R root:magician /home/magician && \
    chmod -R 750 /home/magician

EXPOSE 5000

CMD ["/usr/sbin/xinetd", "-d"]
