FROM python:3.7
ENV PYTHONUNBUFFERED 1 \
    TZ=Europe/Moscow

RUN mkdir /app
COPY . /app/
WORKDIR /app

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && apt-get -y install apt-utils \
    && DEBIAN_FRONTEND=noninteractive ACCEPT_EULA=Y apt-get -y install msodbcsql17 \
    && DEBIAN_FRONTEND=noninteractive ACCEPT_EULA=Y apt-get -y install mssql-tools \
    && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile \
    && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc \
    && /bin/bash -c 'source ~/.bashrc' \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install unixodbc-dev \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install libgssapi-krb5-2 \
    && pip install --upgrade pip setuptools wheel pipenv \
    && pipenv install --system --deploy

EXPOSE 8000
