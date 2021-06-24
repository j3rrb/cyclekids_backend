FROM python:3.9.5-alpine3.13

RUN apk add --no-cache postgresql-libs && \
apk add --no-cache --virtual .build-deps gcc musl-dev postgres-dev && \
python -m pip install pipenv && \
pipenv install

WORKDIR /app/cyclekids_backend
COPY . .
CMD pipenv run python manage.py runserver

EXPOSE 80