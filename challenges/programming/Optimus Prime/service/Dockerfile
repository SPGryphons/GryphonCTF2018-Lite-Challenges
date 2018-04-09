FROM node:9-alpine

RUN adduser -D prime

COPY ./banner.txt /home/prime/
COPY ./server.js /home/prime/
COPY ./data.json /home/prime/

WORKDIR /home/prime

RUN chown -R root:prime /home/prime && \
    chmod -R 750 /home/prime

USER prime
ENV HOME=/home/prime
EXPOSE 5001

CMD ["node", "/home/prime/server.js"]
