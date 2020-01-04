import urllib.request, json 
with urllib.request.urlopen("http://127.0.0.1:8000") as url:
    data = json.loads(url.read().decode())
    print(data)