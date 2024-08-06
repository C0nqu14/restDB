# Exemplo Python RestDB

Este projeto demonstra como fazer operações básicas (GET, POST, PUT, DELETE) em um banco de dados RestDB usando Python. O código de exemplo inclui uma solicitação GET para recuperar dados.

### Pré-requisitos
- [Python 3.8"](https://img.shields.io/badge/_Python)
- Biblioteca requests(pode ser instalada via pip install requests)

### Código

```Python
import requests
import json

_id = "66b16b4dea8c604700019a37"

#endpoint PUT & DELETE
#url = f"https://teste-2078.restdb.io/rest/teste/{_id}"

#endpoint GET
url = "https://teste-2078.restdb.io/rest/teste"

headers = {
    "content-type": "application/json",
    "x-apikey": "599f35f116feca4e6a827b91dcd351d06c2b4"
}

data = json.dumps({
    "_id": 1,
    "Nome": "João Manuel Conquia",
    "Idade": 18
})

response = requests.get(url, headers=headers)
#response = requests.post(url, headers=headers, data=data)
#response = requests.put(url, headers=headers, data=data)
#response = requests.delete(url, headers=headers)

print(response.status_code)
print(response.json())

```
### Descrição

1. GET : Recupera dados do banco de dados RestDB.
2. POST : Adiciona novos dados ao banco de dados.
3. PUT : Atualiza dados existentes no banco de dados.
4. DELETE : Remove dados do banco de dados.
   
O código fornecido está configurado para fazer uma solicitação GET. As linhas de código para POST, PUT e DELETE estão comentadas, mas podem ser descommentadas conforme necessário.

### Como usar

- Substitua a URL do endpoint e a chave API pelo seu próprio endpoint e chave API do RestDB.
- Descomente a linha correspondente à operação desejada (POST, PUT, DELETE) e comente a linha atual (GET).
- Execute um script Python.

### Nota
- se de que você tem restrições para acessar e modificar o banco de dados RestDB e que as chaves e endpoints usados ​​são válidos.
