docker build -t cookiemonster .
docker run -dt -p 44443:80 --name web-cookie cookiemonster
docker start web-cookie
