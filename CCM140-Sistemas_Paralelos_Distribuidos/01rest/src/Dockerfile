FROM python:3.13.7-alpine3.21

WORKDIR /app

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app/* .

CMD ["fastapi", "run", "/app/main.py"]
