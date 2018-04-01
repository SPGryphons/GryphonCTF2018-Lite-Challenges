FROM node:9-alpine

RUN adduser -D flag

COPY ./banner.txt /home/flag/
COPY ./server.js /home/flag/

RUN chown -R root:flag /home/flag && \
    chmod -R 750 /home/flag

USER flag
ENV HOME=/home/flag
WORKDIR /home/flag
EXPOSE 5003

CMD ["node", "/home/flag/server.js"]