#https://newsapi.org/v2/everything?q=bitcoin&from=2021-01-03&sortBy=publishedAt&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=apple&from=2021-07-02&to=2021-07-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#"https://newsapi.org/v2/everything?q=android&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=google&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=university&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=college&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=school&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=education&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=remotework&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=automation&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=travel&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=cricket&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=sports&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=sitcom&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=technology&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=cloudcomputing&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=bigdata&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=drones&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=computing&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=artificialintelligence&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=machinelearning&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=datascience&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=topology&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
#https://newsapi.org/v2/everything?q=politics&from=2021-07-02&to=2021-06-02&sortBy=popularity&apiKey=67bae7a86a1a498c88fb875b2b5e08c6
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

