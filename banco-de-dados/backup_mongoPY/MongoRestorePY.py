import subprocess
from pymongo import MongoClient
import os

client = MongoClient()
backup = "C:/MongoBackupsSave"

def restoreMongo(database):
    backupRoute = input("Rota do backup desejado:\n")
    
    comando = f"mongorestore --host localhost --port 27017 --db {database} {backupRoute}"
    subprocess.run(comando, shell=True)

databases = client.list_database_names()
print('0. [todos]')

for i, v in enumerate(databases):
    print(f'{i+1}. [{v}]')

bancos = int(input('>> '))

if bancos > 0:
    restoreMongo(databases[bancos - 1])
elif bancos == 0:
    for i, v in enumerate(databases):
        restoreMongo(v)

client.close()