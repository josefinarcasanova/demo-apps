# Import Node image
FROM node:lts-alpine3.15

# Copy files into container
COPY . .

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