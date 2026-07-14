FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Build the Astro project
RUN npm run build

# Expose the default Astro preview port
EXPOSE 4321

# Serve the production build using Astro preview
CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0"]
