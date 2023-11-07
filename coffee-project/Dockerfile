FROM node:18

WORKDIR /usr/src/app

COPY ./coffee-project/package*.json ./

RUN npm install

COPY ./coffee-project .

EXPOSE 3000

CMD ["npm", "start"]
