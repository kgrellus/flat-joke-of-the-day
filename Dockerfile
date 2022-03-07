FROM python:3

WORKDIR /usr/src/app

RUN pip install pipenv

COPY Pipfile* /usr/src/app/

RUN pipenv install

COPY .env /usr/src/app/

COPY docker/run.sh /usr/src/app/

COPY main.py /usr/src/app/

CMD [ "./run.sh" ]
