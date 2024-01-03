FROM ubuntu:20.04
ENV TZ=America/Chicago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update --fix-missing
RUN apt-get upgrade -y --fix-missing
RUN apt-get install -y docker.io
RUN apt-get install -y git
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt-get install -y nodejs
RUN npm install semistandard --global
RUN npm install request --global
RUN export NODE_PATH=/usr/lib/node_modules
RUN npm install --save-dev jest
RUN npm install --save-dev babel-jest @babel/core @babel/preset-env
RUN npm install --save-dev eslint