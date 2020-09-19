FROM python:3.7-alpine

WORKDIR /app

# Webinterface will run on port 5000
EXPOSE 5000

# Copy files to /app directory, install requirements
COPY . /app

# Install dependencies for install
RUN apk add --no-cache --virtual .deps \
        musl-dev gcc git && \
    apk add --no-cache libffi-dev libressl-dev

RUN pip install -r /app/requirements.txt

ENV FLASK_DEBUG=1 \
    FLASK_CONFIG="development"

# Start application
CMD [ "python", "./run_dev.py" ]
