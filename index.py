
import json, requests

temp = {
    "jsonrpc": "2.0",
    "method": "deploy",
    "params": {
        "type": 1,
        "chaincodeID": {
            "path": "http://gopkg.in/ibm-blockchain/example02.v2/chaincode"
        },
        "ctorMsg": {
            "function": "init",
            "args": [
                "a",
                "100",
                "b",
                "200"
            ]
        },
        "secureContext": "dashboarduser_type1_2"
    },
    "id": 1
} 

dados =  json.dumps(temp)

# dados  = json.dumps(dados)
 
# response = requests.post("https://ae2d9e75a6114eee9bb6bf77c739c9ef-vp2.us.blockchain.ibm.com:5003/chaincode", data=dados)

# response = requests.post("http://localhost:3000/api/visitors", data=dados)

# response = requests.get("http://viacep.com.br/ws/07600000/json/")

# response = requests.get("https://4cb3d49079a742628525f43946ace9b9-vp0.us.blockchain.ibm.com:5001/chain")

# print aux

def postApi ():
    response = requests.post("https://ae2d9e75a6114eee9bb6bf77c739c9ef-vp2.us.blockchain.ibm.com:5003/chaincode", data=dados)
    print response.content
    print response.status_code
    

def getApi():
    response = requests.get("https://4cb3d49079a742628525f43946ace9b9-vp0.us.blockchain.ibm.com:5001/chain/blocks/1")
    print response.content
    print response.status_code

while ( 1==1):
    num = input('Entre com o 1 para inserir ou 2 para consultar: ')
    if num == 1:
        postApi()
    else:
        getApi()


# response = requests.get("http://jsonplaceholder.typicode.com/comments")

# print json.loads(response.content)

# print response.content

# print response.status_code



