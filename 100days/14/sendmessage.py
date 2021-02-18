import urllib.parse
import http.client
import json

def main():
    host = '106.ihuyi.com'
    sms_send_uri ="/webservice/sms.php?method=Submit"
    # 请填入自己的账号和密码
    params = urllib.parse.urlencode({'account':'C39638515','password':'d7594a3339eb37fab8ae8744ff7c4a9a','content':' \
                   您的验证码是：1234。请不要把验证码泄露给其他人。','mobile':'17302241695','format':'json'} )
    print(params)
    headers = {'Content-Type':'application/x-www-form-urlencoded','Accept':'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()

if __name__ == '__main__':
    main()







