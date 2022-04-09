# Se more info here: https://docs.docker.com/language/python/build-images/

# Import Python
FROM python:latest

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy application code
COPY /src /src

# Copy cert file
COPY db_cert /etc/ssl/certs/db_cert

# Change directory to source code
WORKDIR /src

# Run main script
CMD [ "python", "./main.py" ]