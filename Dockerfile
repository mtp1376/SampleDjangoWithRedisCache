FROM python:3.9

RUN mkdir /code
WORKDIR /code/

COPY requirements.txt /code/

RUN pip install -r /code/requirements.txt

COPY . /code/

ENTRYPOINT [ "/code/docker-entrypoint.sh" ]
