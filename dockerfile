FROM ktzr/python-pip

LABEL maintainer="ishanj58@gmail.com"

COPY . /test_docker

WORKDIR /test_docker

RUN pip install --upgrade pip

RUN pip install pandas && pip install requests

CMD [ "python", "./order_delete.py" ]
