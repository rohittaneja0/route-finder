FROM python:3.9.0-alpine
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN python3 -m pip install --upgrade pip setuptools wheel
RUN pip install -r /code/requirements.txt
COPY . /code/api
WORKDIR /code/api
EXPOSE 8080/tcp
CMD ["flask", "run"]
