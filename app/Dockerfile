# build stage
FROM node:slim AS build

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . .

RUN npm ci

RUN npm run build

# serve stage
FROM node:slim as serve

ENV APP_HOME /app

WORKDIR $APP_HOME

RUN npm i -g serve

COPY --from=build /app/dist ./dist

EXPOSE 3000

CMD ["serve", "-s", "dist", "-l", "3000"] 
