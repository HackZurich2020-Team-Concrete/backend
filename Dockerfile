FROM python:3.7-alpine

# Create user with home directory and no password and change workdir
RUN adduser -Dh /app app
WORKDIR /app
# Webinterface will run on port 8080
EXPOSE 8080

# Install bjoern and dependencies for install (we need to keep libev)
RUN apk add --no-cache --virtual .deps \
        musl-dev gcc git && \
    apk add --no-cache libev-dev && \
    apk add --no-cache libffi-dev libressl-dev && \
    pip install bjoern

# Copy files to /app directory, install requirements
COPY ./ /app

RUN pip install -r /app/requirements.txt

# Cleanup dependencies
RUN apk del .deps

# Switch user
USER app

# Start application
CMD [ "python3", "run_prod.py" ]
