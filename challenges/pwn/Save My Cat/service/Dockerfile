FROM debian:jessie

RUN apt-get update && apt-get install -y openssh-server
# password is gryphonctflite2018
RUN useradd -m player -p '$6$rxyZfCN5$FwB3ST0C.Xu0VgnuwXsJ.2juhgg5CGdJXGUhHIC5RpG.ESZUd0p3luc6n5cKUY698G1QpssuEF9niPRc73gOH/' -s /bin/rbash

RUN mkdir /home/player/progs && \
    ln -s /bin/ls /home/player/progs/ && \
    ln -s /bin/cat /home/player/progs/

RUN echo 'alias cat=' >> /home/player/.bashrc && \
    echo 'export PATH=/home/player/progs' >> /home/player/.bashrc

COPY ./flag.txt /home/player/
RUN mv /home/player/flag.txt /home/player/.flag.txt

RUN chown -R root:player /home/player && \
    chmod -R 750 /home/player

COPY ./motd /etc/
RUN sed -i -e 's/Subsystem/#Subsystem/g' /etc/ssh/sshd_config
RUN service ssh start
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]