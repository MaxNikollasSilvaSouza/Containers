# Como conectar a uma api dentro de um container em um banco em outro container ?

```
conectar no banco dentro de outro container (nome do banco + ip do banco dentro do container + a porta)
mongoengine.connect(host="mongodb://172.17.0.3:27017" )
```

Para baixar um banco dentro do container, basta baixar uma imagem e seguir as orientações (que te servem) no site [Docker hub:](https://hub.docker.com/_/mongo?tab=description)


Comando para identificar o IP do container com o banco:
``` 
docker ps
```

Copie o Container ID e digite o comando: 
``` 
docker inspect <aqui voce coloca o ID do container que você quer inspecionar>
```

após isso, basta pegar o IPAddress e colocar na sua API assim como mostrado no inicio deste documento.
