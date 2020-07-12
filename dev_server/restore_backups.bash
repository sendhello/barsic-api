#!/bin/bash
docker exec -it dev_server_bars_db_1 mkdir /var/opt/mssql/backup
docker cp dev_server/backups/AquaPark_Ulyanovsk.bak dev_server_bars_db_1:/var/opt/mssql/backup
docker cp dev_server/backups/Beach.bak dev_server_bars_db_1:/var/opt/mssql/backup
docker cp dev_server/backups/bitrix_transaction.bak dev_server_bars_db_1:/var/opt/mssql/backup
docker exec -it dev_server_bars_db_1 /opt/mssql-tools/bin/sqlcmd \
   -S localhost -U SA -P 'MSSQL@1234' \
   -Q 'RESTORE DATABASE AquaPark_Ulyanovsk FROM DISK = "/var/opt/mssql/backup/AquaPark_Ulyanovsk.bak" WITH MOVE "SkiBars2" TO "/var/opt/mssql/data/AquaPark_Ulyanovsk.mdf", MOVE "SkiBars2_log" TO "/var/opt/mssql/data/AquaPark_Ulyanovsk_log.ldf"'
docker exec -it dev_server_bars_db_1 /opt/mssql-tools/bin/sqlcmd \
   -S localhost -U SA -P 'MSSQL@1234' \
   -Q 'RESTORE DATABASE Beach FROM DISK = "/var/opt/mssql/backup/Beach.bak" WITH MOVE "Ski2Db_AlexBay" TO "/var/opt/mssql/data/Beach.mdf", MOVE "Ski2Db_AlexBay_log" TO "/var/opt/mssql/data/Beach_log.ldf"'
docker exec -it dev_server_bars_db_1 /opt/mssql-tools/bin/sqlcmd \
   -S localhost -U SA -P 'MSSQL@1234' \
   -Q 'RESTORE DATABASE bitrix_transaction FROM DISK = "/var/opt/mssql/backup/bitrix_transaction.bak" WITH MOVE "bitrix_transaction" TO "/var/opt/mssql/data/bitrix_transaction.mdf", MOVE "bitrix_transaction_log" TO "/var/opt/mssql/data/bitrix_transaction_log.ldf"'
