FROM ubi8/python-39
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN python3 -m pip install --upgrade pip setuptools wheel
RUN pip install -r /code/requirements.txt
COPY . /code/api
WORKDIR /code/api
EXPOSE 8080/tcp
CMD [ "python", "./app.py" ]
