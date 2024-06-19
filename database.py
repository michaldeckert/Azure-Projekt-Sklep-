import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from variables import usernameV, passwordV, serverV, databaseV

server = serverV
database = databaseV
username = usernameV
password = passwordV

driver = '{ODBC Driver 18 for SQL Server}'

# odbc_str = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:sqlserversklepprojekt.database.windows.net,1433;Database=sklepMuzyczny;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'
odbc_str = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;UID='+username+';DATABASE='+ database + ';PWD='+ password
connect_str = 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus(odbc_str)

print(connect_str)

engine = create_engine(connect_str)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind = engine)

Base = declarative_base()
