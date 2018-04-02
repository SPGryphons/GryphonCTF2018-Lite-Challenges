docker build -t cookiemonster .
docker run --restart always -d -p 44443:80 --name web-cookie cookiemonster
docker start web-cookie
