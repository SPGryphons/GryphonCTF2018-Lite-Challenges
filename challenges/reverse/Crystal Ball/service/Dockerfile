FROM node:9-alpine

RUN adduser -D magic

COPY ./banner.txt /home/magic/
COPY ./server.js /home/magic/
RUN npm i --prefix /home/magic/ ntp-client

RUN chown -R root:magic /home/magic && \
    chmod -R 750 /home/magic

USER magic
ENV HOME=/home/magic
WORKDIR /home/magic
EXPOSE 5002

CMD ["node", "/home/magic/server.js"]
