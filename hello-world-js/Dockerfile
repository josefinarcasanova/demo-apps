# Import Node image
FROM --platform=linux/amd64 node:current-alpine

# Set working directory
WORKDIR /usr/app

# Copy files into container
COPY ./ /usr/app

# Install dependencies
RUN npm install

# Define env variable PORT
# ENV PORT=8080

# Expose PORT
# EXPOSE ${PORT}

# Run program
CMD [ "node", "server.js" ]

# See https://stackoverflow.com/questions/46917831/how-to-load-several-environment-variables-without-cluttering-the-dockerfile
# ENTRYPOINT ["sh", "./start.sh"]