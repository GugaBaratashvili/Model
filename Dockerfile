From node:6.10.2

Add ./ /code/

Run npm install

RUN npm install -g pm2

EXPOSE 3000

ENTRYPOINT ['pm2-docker' 'app.js']
