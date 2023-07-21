import urllib.request
import json
with urllib.request.urlopen('https://api.github.com/users/zzajang-bro/repos') as response:
    content = response.read()
dat = json.loads(content)
#print(dat) // array of dict
nameList = [el['name'] for el in dat]
for i in range(len(nameList)):
    print(nameList[i])
input()
