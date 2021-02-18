import requests

resp = requests.get('http://www.baidu.com/index.html')
print(resp.status_code)
print(resp.headers)
print(resp.cookies)
print(resp.content.decode('utf-8'))

resp = requests.post('http://httpbin.org/post',data={'name':'Hao','age':40})
print(resp.text)
data = resp.json()
print(type(data))