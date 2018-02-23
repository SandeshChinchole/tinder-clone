FROM node:8

RUN apt-get update && apt-get install -y build-essential python

#Install deps
RUN mkdir /app
ADD app /app/
RUN cd /app && npm install && npm run build
RUN npm -g install serve

#Add all source code

#RUN cd /app 

WORKDIR /app

#Default command
CMD ["serve", "-s", "public", "-p", "8080"]
