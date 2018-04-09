FROM ubuntu:latest
RUN mkdir -p /usr/src/PartyInvite
WORKDIR /usr/src/PartyInvite
COPY PartyServer.c .
RUN apt-get update &&\
	apt-get install build-essential nmap -y 
RUN cc PartyServer.c -fno-stack-protector -Wl,--section-start=.special=0x1a1b1c1d -o start
CMD ["ncat", "-kl", "50000", "-e", "./start"]