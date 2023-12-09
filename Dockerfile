FROM python:3.12.0-alpine3.18

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install poetry
RUN apk add --no-cache \
    poetry

# copy file project in iso
WORKDIR /app
COPY pyproject.toml poetry.lock /app/

# install dependencies with poetry
RUN poetry config virtualenvs.create false && poetry install --only main --no-interaction --no-ansi

# Copy the rest of the project files
COPY . /app

# Optional: set the working directory
WORKDIR /app

# create migrations
#RUN poetry run python manage.py migrate --noinput

# create collectstatic
#RUN poetry run python manage.py collectstatic --noinput

# Optional: specify the default command when starting the container
CMD poetry run python manage.py runserver 0.0.0.0:8000
