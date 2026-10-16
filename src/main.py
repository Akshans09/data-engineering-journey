import requests

url = "https://jsonplaceholder.typicode.com/posts"
#request sent to API 
response = requests.get(url)

#this is to convert response to python data
data= response.json()

print(len(data))
print(data[0])


#save to file
import json

with open("data/raw.json","w") as f:
    json.dump(data,f)

#i just pulled data from internet, converted it to python data and then saved the data locally. (data ingestion)