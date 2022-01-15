FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli@4.5.15 -g

COPY package.json .
COPY yarn.lock .
RUN yarn install

CMD ["yarn", "serve"]