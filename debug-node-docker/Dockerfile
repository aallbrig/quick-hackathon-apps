FROM node:latest

WORKDIR /usr/app

COPY ./package.json /usr/app/package.json

RUN npm install

COPY . /usr/app

ENV PORT 3000
ENV DEBUG_PORT 9229

EXPOSE $PORT
EXPOSE $DEBUG_PORT

CMD npm run start-dev

