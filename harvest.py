
import requests
import json
response = requests.get("https://newsapi.org/v2/everything?q=iot&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6")
print(response)

url = ('https://newsapi.org/v2/everything?'
       'q=iot&'
       'from=2021-07-02&'
       'to=2021-06-02&'
       'sortBy=popularity&'
       'apiKey=67bae7a86a1a498c88fb875b2b5e08c6')

r = requests.get(url)
x=r.json()
with open("sample28.json", "w") as outfile:
    json.dump(x, outfile)
print("done")

