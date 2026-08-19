# Exercício 1: Container com Python, dados aleatórios e réplicas de container

Esta pasta contém os seguintes arquivos:
- `Dockerfile` que usa como base uma imagem do Python disponível no [Docker Hub](https://hub.docker.com/_/python);
- `docker-compose.yaml` que usa a imagem criada com o arquivo anterior para executar réplicas do mesmo container;
- `src/main.py` um script em Python que gera números aleatórioas a cada meio segundo.

## Execução local do script em Python

O script no arquivo `src/main.py` é usado somente para gerar dados aleatórios (para facilitar o uso deste exercício, imagine que são dados medidos por sensores (e.g., temperatura, humidade, etc.) ou métricas tiradas de algum servidor (e.g., uso de CPU, RAM, etc.)) e está comentado linha a linha para facilitar a explicação.

```python
# importa as funções necessárias para gerar números aleatórios
# e fazer o script esperar por um tempo especificado
import random
from time import sleep

random.seed()  # inicializa o seed do gerador de números aleatórios com o horário atual

## repete para sempre pois queremos que os dados não parem de ser gerados
while True:
    print(random.randint(1,10), flush=True) # gera e exibe o valor aleatório
    sleep(0.5)  # espera meio segundo antes de continuar
```

A única diferença do que normalmente usamos é a opção `flush=True` na função `print`. Esta opção é usada para que o container exiba o resultado assim que a linha for executada.

Para executar o script podemos executar pelo terminal a linha `python src/main.py` e veremos um número aleatório sendo exebido em uma linha a cada meio segundo.

Com este script funcionando, podemos criar um container que executa este script quando for iniciado.

## Criação do container e execução da instância

Para este exercício vamos usar a imagem oficial do container de Python disponibilizado no Docker Hub. O `Dockerfile` que vamos usar deve:
1. Usar a imagem oficial do Python;
2. Copiar o código que está na pasta `src` para dentro do container, fazendo parte da imagem gerada;
3. Executar o código copiado quando executamos o container.

O resultado final é o seguinte arquivo:

```Dockerfile
FROM python:3.13.7-alpine3.21

WORKDIR /app

COPY src .

CMD ["python", "main.py"]
```

Neste `Dockerfile`, a primeira linha especifica a imagem que será usada, ou seja, estamos usando como base a imagem que contém o Python na versão 3.13.7 instalado em uma imagem da distribuição Alpine Linux na versão 3.21.

Em seguida definimos que o diretório em que tudo será executado na criação da imagem e será também o diretório usado pelo shell quando o container é iniciado é o `/app`. A linha seguinte realiza a cópia (`COPY`) do conteúdo da pasta `src` para a pasta atual (representada pelo `.`) do container (neste caso, `/app`).

A última linha passa o comando que será executado quando iniciarmos o container. O `CMD` recebe uma lista de strings do que deve ser executado e neste caso é o equivalente a executarmos `python main.py` no terminal.

Com o `Dockerfile` salvo, podemos executar `docker build -t cc7261:random .` de dentro da pasta atual para gerar uma imagem de nome `cc7261` com a tag `random` usando como contexto a pasta atual (novamente representada pelo `.` no final da linha).

Por fim, podemos executar esta imagem usando `docker run cc7261:random` e, se tudo estiver certo, os números aleatórios deverão aparecer na tela da mesma forma de quando executamos o script de fora do container.

Se quisermos executar mais do que um container que gere dados aleatórios, ainda precisamos abrir mais do que um terminal e executar container por container, parecido com o que fazíamos executando o script local. Para facilitar, vamos usar o docker compose para executar algumas réplicas do container.

## Docker-compose para execução e réplicas do container

Enquanto o `Dockerfile` especifica como a imagem do container será criada, o `docker-compose.yaml` especifica como uma ou mais imagens serão executadas. O arquivo segue a [especificação do YAML](https://yaml.org/spec/1.2.2/) para a descrição dos serviços (i.e., containers) que queremos executar e permite a descrição dos mesmos atributos que temos disponíveis com o `docker run`.

Para facilitar a explicação, o conteúdo do arquivo está a seguir:
```yaml
services:

  py-random:
    build:
        context: .
        dockerfile: Dockerfile
    image: cc7261:random
    volumes:
      - ./src:/app
    deploy:
      replicas: 10
````

A primeira linha especifica que as definições a seguir são dos serviços que serão executados. Em seguida definimos que um serviço chamado de `py-random` será construído (`build`) usando a pasta atual (`.`) como contexto (`context`) e usará o arquivo `Dockerfile` para construir a imagem usada pelo serviço (`dockerfile`), sendo o resultado final (`image`) a imagem `cc7261:random`. Neste serviço teremos um volume montado (`volumes`) que montará a pasta `./src` local na pasta `/app` que está dentro do container. Por fim, na execução deste `docker-compose.yaml` (`deploy`) serão criados 10 containers executando o mesmo código (`replicas: 10`).

Ao executar o comando `docker compose up` no terminal, veremos a criação de cada instância da imagem que foi criada na seção anterior sendo que cada parte será nomeada `py-random-n` em que `n` é um número dado à réplica do container.
