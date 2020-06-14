## Dockerized BombSquad Server

An unofficial docker image for server app of [BombSquad Game](https://www.froemling.net/apps/bombsquad)


### Usage


```bash
docker run -d -it \
           -p 43210:43210/udp \
           --name bombsquad \
           -v `pwd`/config.py:/app/bombsquad-server/config.py \
           alibo/bombsquad
```

You can use **config.py** in this repo. 



### Dockerhub

See: https://hub.docker.com/r/alibo/bombsquad
