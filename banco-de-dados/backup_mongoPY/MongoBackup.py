import subprocess
from datetime import datetime
from pymongo import MongoClient
import os

client = MongoClient()
backup = "C:/MongoBackupsSave"
if not os.path.exists(backup):
    os.makedirs(backup)

def backupMongoDump(database):
    horaAtual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = f"{backup}/{database}_{horaAtual}"

    subprocess.run(f"mkdir {backup_file}", shell=True)

    comando = f"mongodump --host localhost --port 27017 --db {database} --out {backup_file}"
    subprocess.run(comando, shell=True)



databases = client.list_database_names()
print('0. [todos]')

for i, v in enumerate(databases):
    print(f'{i+1}. [{v}]')

bancos = int(input('>> '))

if bancos > 0:
    backupMongoDump(databases[bancos - 1])
elif bancos == 0:
    for i, v in enumerate(databases):
        backupMongoDump(v)

client.close()
