FROM ubuntu:latest

ENV HOME /home/PartyInvite
RUN useradd -m PartyInvite
WORKDIR $HOME

RUN apt-get update
RUN apt-get install libc6-i386 xinetd -y

COPY ./start ./
COPY ./partyinvite /etc/xinetd.d/

CMD ["xinetd", "-d"]
