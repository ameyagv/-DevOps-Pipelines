FROM node:18

WORKDIR /usr/src/app

RUN cd coffee-project

COPY package*.json ./

RUN npm ci

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
