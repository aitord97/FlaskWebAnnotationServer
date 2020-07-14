FROM python:3.7-alpine

ADD ./src /server

WORKDIR /server

ENV FLASK_APP app.py

ENV FLASK_RUN_HOST 0.0.0.0

RUN apk update && apk add --no-cache gcc musl-dev linux-headers

RUN pip3 install pymongo

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD [ "python3", "app.py" ]