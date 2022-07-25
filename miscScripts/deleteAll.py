import requests
import secrets
import json
from requests_toolbelt.utils import dump



baseUrl = secrets.BASE_URL + "query"

query = {
    "items": []
}

payload = json.dumps(query)

headersDict = {
    'X-API-Key' : secrets.PROJECT_KEY,
    'Content-Type': 'application/json'
}


while True:
    response = requests.post(url=baseUrl, headers=headersDict, data=payload)
    jsonified = json.loads(response.text)
    if (len(jsonified["items"])==0):
        print("Done!")
        break

    for item in jsonified["items"]:
        delResponse = requests.delete(url=secrets.BASE_URL + "items/" + item["key"], headers=headersDict)
        data = dump.dump_all(delResponse)