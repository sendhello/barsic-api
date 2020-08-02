# Barsic-API

## Запуск тестового сервера
* Сделать копию файла `.env.example` с названием `.env`
* Запустить docker-compose
```console
$ docker-compose -f dev_server/docker-compose.yml up
```
* После запуска контейнеров(!!!) скопировать в папку `dev_server/bars_db_backup` бэкапы и переименовать их при необходимости в:
`AquaPark_Ulyanovsk.bak`, `Beach.bak` и `bitrix_transaction.bak`
* Распаковать бэкапы баз данных:
```bash
dev_server/restore_backups.bash
```
* Если возникает ошибка `Permission denied`, сделать bash-файл исполняемым и попробовать снова
```bash
chmod +x dev_server/restore_backups.bash
```

#### Ручная распаковка бекапов баз Барса в тестовую БД (при возникновении проблем с автоматической):
*(Примеры указаны для БД AquaPark_Ulyanovsk)*
* Скопировать бекапы в Docker-контейнер :
```bash
docker exec -it dev_server_bars_db_1 mkdir /var/opt/mssql/backup
docker cp AquaPark_Ulyanovsk.bak dev_server_bars_db_1:/var/opt/mssql/backup
```
* Вывести список логических имен файлов и путей внутри резервной копии
```bash
docker exec -it dev_server_bars_db_1 /opt/mssql-tools/bin/sqlcmd -S localhost \
   -U SA -P 'MSSQL@1234' \
   -Q 'RESTORE FILELISTONLY FROM DISK = "/var/opt/mssql/backup/AquaPark_Ulyanovsk.bak"' \
   | tr -s ' ' | cut -d ' ' -f 1-2
```
Восстановить базу данных внутри контейнера. 
Укажите новые пути для каждого из файлов в предыдущем шаге
```bash
docker exec -it dev_server_bars_db_1 /opt/mssql-tools/bin/sqlcmd \
   -S localhost -U SA -P 'MSSQL@1234' \
   -Q 'RESTORE DATABASE AquaPark_Ulyanovsk FROM DISK = "/var/opt/mssql/backup/AquaPark_Ulyanovsk.bak" WITH MOVE "SkiBars2" TO "/var/opt/mssql/data/AquaPark_Ulyanovsk.mdf", MOVE "SkiBars2_log" TO "/var/opt/mssql/data/AquaPark_Ulyanovsk_log.ldf"'
```
Подробнее о востановлении баз данных на сервера MSSQL-Server Linux в Docker-контейнере:
https://docs.microsoft.com/ru-ru/sql/linux/tutorial-restore-backup-in-sql-server-container?view=sql-server-ver15