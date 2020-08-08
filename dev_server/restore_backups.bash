#!/bin/bash
echo '======================== Start restore database ========================'
docker exec -it dev_server_bars_db_1 ls /var/opt/mssql/backup
echo 'Restore database AquaPark_Ulyanovsk'
docker exec -it dev_server_bars_db_1 /opt/mssql-tools/bin/sqlcmd \
   -S localhost -U SA -P 'MSSQL@1234' \
   -Q 'RESTORE DATABASE AquaPark_Ulyanovsk FROM DISK = "/var/opt/mssql/backup/AquaPark_Ulyanovsk.bak" WITH MOVE "SkiBars2" TO "/var/opt/mssql/data/AquaPark_Ulyanovsk.mdf", MOVE "SkiBars2_log" TO "/var/opt/mssql/data/AquaPark_Ulyanovsk_log.ldf"'
echo 'Restore database Beach'
docker exec -it dev_server_bars_db_1 /opt/mssql-tools/bin/sqlcmd \
   -S localhost -U SA -P 'MSSQL@1234' \
   -Q 'RESTORE DATABASE Beach FROM DISK = "/var/opt/mssql/backup/Beach.bak" WITH MOVE "Ski2Db_AlexBay" TO "/var/opt/mssql/data/Beach.mdf", MOVE "Ski2Db_AlexBay_log" TO "/var/opt/mssql/data/Beach_log.ldf"'
echo 'Restore database bitrix_transaction'
docker exec -it dev_server_bars_db_1 /opt/mssql-tools/bin/sqlcmd \
   -S localhost -U SA -P 'MSSQL@1234' \
   -Q 'RESTORE DATABASE bitrix_transaction FROM DISK = "/var/opt/mssql/backup/bitrix_transaction.bak" WITH MOVE "bitrix_transaction" TO "/var/opt/mssql/data/bitrix_transaction.mdf", MOVE "bitrix_transaction_log" TO "/var/opt/mssql/data/bitrix_transaction_log.ldf"'
echo '========================= Restore databases done! ========================='