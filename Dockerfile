FROM python:3

WORKDIR /usr/src/app

RUN pip install pipenv

COPY main.py /usr/src/app/
COPY Pipfile* /usr/src/app/
COPY .env /usr/src/app/

COPY docker/run.sh /usr/src/app/

RUN pipenv install

CMD [ "./run.sh" ]
