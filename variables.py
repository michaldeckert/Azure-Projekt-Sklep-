import os
# AZURE_SQL_CONNECTIONSTRING = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:sqlserversklepprojekt.database.windows.net,1433;Database=sklepMuzyczny;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'
usernameV = os.getenv('DATABASE_USERNAME')
passwordV = os.getenv('DATABASE_PASSWORD')

if not usernameV or not passwordV:
    raise ValueError("Zmienne środowiskowe DATABASE_URL lub SECRET_KEY nie zostały ustawione!")

print(f"USERNAME: {usernameV}")
print(f"PASSWORD: {passwordV}")
