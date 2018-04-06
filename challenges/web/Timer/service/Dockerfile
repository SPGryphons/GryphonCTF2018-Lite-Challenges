FROM php:7.0-apache
RUN apt-get update
RUN rm -rf /var/www/html/ && mkdir -p /var/www/html
COPY ./index.html /var/www/html/
COPY ./flag.html /var/www/html/
COPY ./.htaccess /var/www/html/
COPY ./styles.css /var/www/html/
COPY ./NKflag.jpg /var/www/html/
COPY ./usflag.png /var/www/html/
