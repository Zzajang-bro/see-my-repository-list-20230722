import urllib.request
import json
with urllib.request.urlopen('https://api.github.com/users/zzajang-bro/repos') as response:
    content = response.read()
dat = json.loads(content)
#print(dat) // array of dict
nameList = [[el['name'], el['description']] for el in dat]
print(json.dumps(nameList, ensure_ascii=False))
input()
# 참고: 2차원 JSON 표로 보기
# https://github.com/Zzajang-bro/2d-json-viewer-20230722
