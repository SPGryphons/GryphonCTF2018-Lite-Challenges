FROM ubuntu:latest

ENV name=candyFlow
ENV HOME=/home/$name

RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y xinetd
RUN apt-get install -y libc6-i386

RUN useradd --create-home $name

ADD  ./flag.txt ./candyFlow ./exec.sh /home/$name/
ADD ./candyFlowService /etc/xinetd.d

RUN chown -R root:$name /home/$name
RUN chmod -R 750 /home/$name

EXPOSE 12345

CMD ["/usr/sbin/xinetd", "-d"]

