FROM python:3.8
ENV PYTHONUNBUFFERED 1 \
    TZ=Europe/Moscow

RUN mkdir /app
COPY Pipfile Pipfile.lock /app/
WORKDIR /app

# Установка драйвера Microsoft ODBC 17
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

# Понижения уровня безопасности для работы с MSSQL 2014
RUN apt-get update -yqq \
    && apt-get install -y --no-install-recommends openssl \
    && sed -i 's,^\(MinProtocol[ ]*=\).*,\1'TLSv1.0',g' /etc/ssl/openssl.cnf \
    && sed -i 's,^\(CipherString[ ]*=\).*,\1'DEFAULT@SECLEVEL=1',g' /etc/ssl/openssl.cnf\
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8000
