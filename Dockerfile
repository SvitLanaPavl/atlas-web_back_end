FROM ubuntu:20.04
WORKDIR /app
ENV TZ=America/Chicago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update --fix-missing
RUN apt-get upgrade -y --fix-missing
RUN apt-get install -y git
RUN apt-get install -y curl
RUN apt-get install -y python3 python3-pip
RUN pip3 install flasgger
RUN pip3 install flask
RUN apt-get install -y python3-lxml
RUN pip3 install flask_cors
RUN pip3 install jsonschema==3.0.1
RUN pip3 install pathlib2
RUN apt-get install -y mysql-server
RUN pip3 install sqlalchemy
RUN pip3 install mysql-connector-python
RUN apt-get install -y python3-mysqldb
ENV PERSONAL_DATA_DB_USERNAME=root \
    PERSONAL_DATA_DB_PASSWORD=root \
    PERSONAL_DATA_DB_HOST=localhost \
    PERSONAL_DATA_DB_NAME=my_db