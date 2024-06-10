FROM ubuntu:20.04

WORKDIR /app

ENV TZ=America/Chicago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update --fix-missing && \
    apt-get upgrade -y --fix-missing && \
    apt-get install -y git curl python3 python3-pip && \
    apt-get install -y python3-lxml mysql-server && \
    apt-get install -y python3-mysqldb

RUN pip3 install flasgger flask flask_cors jsonschema==3.0.1 pathlib2 sqlalchemy mysql-connector-python

ENV PERSONAL_DATA_DB_USERNAME=root \
    PERSONAL_DATA_DB_PASSWORD=root \
    PERSONAL_DATA_DB_HOST=localhost \
    PERSONAL_DATA_DB_NAME=my_db

# Configure MySQL to allow root login without password
RUN sed -i 's/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/' /etc/mysql/mysql.conf.d/mysqld.cnf && \
    echo "skip-grant-tables" >> /etc/mysql/mysql.conf.d/mysqld.cnf

# Expose MySQL port
EXPOSE 3306

# Initialize MySQL database and create user
RUN service mysql start && \
    mysql -u root -e "CREATE DATABASE IF NOT EXISTS ${PERSONAL_DATA_DB_NAME};" && \
    mysql -u root -e "USE mysql; UPDATE user SET plugin='mysql_native_password' WHERE User='root'; FLUSH PRIVILEGES;"

CMD ["mysqld_safe"]
