from django.db import connections
from barsloader.models import Mastertransaction, Accountstock



def all_piple():
    for a in connections:
        print(a)

    print(Mastertransaction.objects.all().first().mastertransactionid)

    # conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.2.200\MSSQL;UID=sa;PWD=1;DATABASE=AquaPark_Ulyanovsk")
    with connections['aqua'].cursor() as cursor:
        cursor.execute(f"""{''}
            SELECT
                [gr].[c1] as [c11],
                [gr].[StockCategory_Id] as [StockCategory_Id1],
                [c].[Name],
                [c].[NN]
            FROM
                (
                    SELECT
                        [_].[CategoryId] as [StockCategory_Id],
                        Count(*) as [c1]
                    FROM
                        [AccountStock] [_]
                            INNER JOIN [SuperAccount] [t1] ON [_].[SuperAccountId] = [t1].[SuperAccountId]
                    WHERE
                        [_].[StockType] = 41 AND
                        [t1].[Type] = 0 AND
                        [_].[Amount] > 0 AND
                        NOT ([t1].[IsStuff] = 1)
                    GROUP BY
                        [_].[CategoryId]
                ) [gr]
                    INNER JOIN [Category] [c] ON [gr].[StockCategory_Id] = [c].[CategoryId]
           """)

        row = cursor.fetchall()
        print(row)

