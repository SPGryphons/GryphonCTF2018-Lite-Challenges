FROM node:9-alpine

RUN adduser -D liars

COPY ./banner.txt /home/liars/
COPY ./server.js /home/liars/
RUN npm i --prefix /home/liars/ bignumber.js

RUN chown -R root:liars /home/liars && \
    chmod -R 750 /home/liars

USER liars
ENV HOME=/home/liars
WORKDIR /home/liars
EXPOSE 5001

CMD ["node", "/home/liars/server.js"]
