# Use an official Node.js base image
FROM node:18-alpine	

# Set working directory
WORKDIR /app

# Copy files
COPY package*.json ./
COPY app.js .
COPY test.js .

# Install dependencies
RUN npm install

# Default command
CMD ["npm", "test"]
