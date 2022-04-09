# Se more info here: https://docs.docker.com/language/python/build-images/

# Import Python
FROM python:latest

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy application code
COPY . .

# Run main script
CMD [ "python", "./main.py" ]