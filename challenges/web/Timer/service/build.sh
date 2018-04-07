docker build -t timersite .
docker run --restart always -d -p 18135:80 --name web-timer timersite
docker start web-timer
