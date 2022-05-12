# Como fazer o exercicio 1 e 2 com docker compose ?

Basta criar o arquivo .yml do docker compose, (qualquer dúvida, leia o passo a passo do quick start do docker). 

As vezes, assim como nesse caso da API, é necessário buildar o container (docker-compose up --build -d) porque se você colocar apenas "docker-compose up" ele vai dar erro.
```
 docker-compose up --build -d
```

Na conexão com o banco da sua API pode colocar só o nome do banco e a porta porque no arquivo .yml ele vai entender e referenciar o banco 
```
mongoengine.connect(host="mongodb://mongo:27017" )
```

# Explicando passo a passo:
    ```
    version: "3.9"
    services: 
    mongo:  
        image: mongo
        restart: always
        ports:
        - "27017:27017"
    
    api:
        build: 
        dockerfile: Dockerfile
        context: .
        ports:
        - "5000:5000"
    
    ```

    1. Mongo:
        mongo foi o nome que eu escolhi
        image - > Cria a imagem de qualquer banco, só especificar assim como estiver na documentação do Docker-Hub.
        restart -> Se der um problema que impeça o funcionamento do banco, o "restart" faz o banco resetar automaticamente pra sempre permanecer funcionando
        ports - > Especifica a porta que o banco irá funcionar.

    2. API:
        API foi o nome que eu escolhi
        build -> constrói o Dockerfile do caminho especificado.
        context -> Responsável pelo controle de acesso, podendo exigir palavras chave para acesso por exemplo. [Stackoverflow]: (https://stackoverflow.com/questions/56410178/please-explain-the-different-types-of-context-in-yaml-with-proper-examples)
        ports - > Especifica a porta que o banco irá funcionar.


# Observações e Atenções:
    1. Em um arquivo docker compose pode-se ter vários arquivos docker. Como os arquivos são chamados apenas "Docker" sem mudança de nome, eles são separados por pastas para não dar conflito e na hora de referenciar basta apontar o caminho das pastas e do Dockerfile.
    Todos os Dockerfile precisam ser escritos com o "D" maiúsculo (Dockerfile).

    2. Faltou especificar a versão do banco, como eu não coloquei nada, ele pega a versão mais recente automaticamente.

    3. O Dockerfile é responsável por "criar um container", porta apenas uma aplicação. Por outro lado o arquivo .yml com docker-compose é responsável por subir vários containers de uma só vez (tem mais coisas que ele faz, mas preciso pesquisar mais).



