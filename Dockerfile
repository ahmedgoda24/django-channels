FROM python:3.11.4-alpine

WORKDIR /app

# prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# ensure Python output is sent directly to the terminal without buffering
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt



COPY . /app/

RUN python manage.py collectstatic --noinput

# Apply database migrations

RUN python manage.py makemigrations
RUN python manage.py migrate
