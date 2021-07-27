# LadyBug
MPS - LadyBug, software para correção e acompanhamento de bugs 

Requisitos:
- Docker 
- Docker-compose
- Angular 
- Node.js
- Python

Antes de tudo, verifique se não há nada retornando com o comando: 
- sudo docker ps -a 

Caso exista algo, rode o comando:
- sudo docker stop "hash"

Comandos para rodar o back-end:
- virtualenv venv --python=python3.8
- source ./venv/bin/activate 
- pip3 install -r requirements.txt
- sudo docker-compose -f docker-compose.yaml up -d --build 
- sudo docker-compose -f docker-compose.yaml ps 

Os conteiner "database" deve estar up.

Por último:
- python3 server.py

Para rodar o frontend, use o comando:
- npm i 
- ng s

Caso uma das portas já esteja sendo usada, usar o comando:
- sudo fuser -k "port"/tcp 

Comandos para acessar o database pelo Compass:
- localhost:27017
- username: ladybug_root
- password: 123ladybug
- admin 




