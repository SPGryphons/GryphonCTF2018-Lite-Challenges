FROM ubuntu:latest

ENV name=magic2
ENV HOME=/home/$name

RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y xinetd
RUN apt-get install -y libc6-i386

RUN useradd --create-home $name

ADD ./flag.txt ./magic2-server ./exec.sh /home/$name/
ADD ./magic2Service /etc/xinetd.d

RUN chown -R root:$name /home/$name
RUN chmod -R 750 /home/$name

EXPOSE 12345

CMD ["/usr/sbin/xinetd", "-d"]

