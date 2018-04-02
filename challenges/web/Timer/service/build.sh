docker build -t timersite .
docker run --restart always -d -p 44445:80 --name web-timer timersite
docker start web-timer
