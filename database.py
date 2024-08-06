import requests
import json

_id = "66b16b4dea8c604700019a37"

#endpoint PUT & DELETE
#url = f"https://teste-2078.restdb.io/rest/teste/{_id}"

#endpoint GET
url = "https://teste-2078.restdb.io/rest/teste"

headers = {

    "content-type" : "application/json" , 
    "x-apikey" : "599f35f116feca4e6a827b91dcd351d06c2b4"
}

data = json.dumps({

    "_id" : 1 ,
    "Nome" : "João Manuel Conquia" ,  
    "Idade" : 18
})

response = requests.get(url , headers = headers)
#response = requests.post(url , headers = headers , data = data)
#response = requests.put(url , headers = headers , data = data)
#response = requests.delete(url , headers = headers)

print(response.status_code)
print(response.json())