FROM node:latest

ENV DB_HOST=host.docker.internal
ENV DB_USER=username
ENV DB_PASS='password'

WORKDIR /app

COPY ./package.json /app
RUN npm install

COPY . /app

EXPOSE 3000

CMD npm start
