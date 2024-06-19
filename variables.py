import os
# AZURE_SQL_CONNECTIONSTRING = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:sqlserversklepprojekt.database.windows.net,1433;Database=sklepMuzyczny;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'
usernameV = os.getenv('DATABASE_USERNAME')
passwordV = os.getenv('DATABASE_PASSWORD')
databaseV = os.getenv('DATABASE_NAME')
serverV = os.getenv('DATABASE_SERVER')
