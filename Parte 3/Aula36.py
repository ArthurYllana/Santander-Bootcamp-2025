import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH/ 'usurarios.csv', 'w', encoding='utf-8') as arquivos:
        escritor = csv.writer(arquivos)
        escritor.writerow(['id', 'nome'])
        escritor.writerow(['1', 'Maria'])
        escritor.writerow(['2', 'João'])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")