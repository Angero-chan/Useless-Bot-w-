import requests
import random
import hashlib
import time
appid,secret_key = open("翻译appid.txt").read().split()
class Translate:
    def __init__(self):
        self.appid = appid
        self.scretKey = secret_key
    def translate(self,text,fromLang = 'en',toLang='zh'):
        q = text
        fromLang = fromLang
        toLang = toLang
        salt = random.randint(32768,65536)
        sign = self.appid + q + str(salt) + secret_key
        sign = self.get_md5(sign)
        url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        data = {'q':q,
                'from':fromLang,
                'to':toLang,
                'appid':self.appid,
                'salt':salt,
                'sign':sign}
        response = requests.post(url,data=data)
        result = response.json()
        #print(result)
        result = result['trans_result'][0]['dst']
        print(time.strftime("%Y-%m-%d %H:%M:%S"),"翻译结果:",result)
        return result
    def get_md5(self,string):
        h = hashlib.md5()
        h.update(string.encode('utf-8'))
        return h.hexdigest()
if __name__ == '__main__':
    t = Translate()
    #txt = open("ReadMeFirst.txt").read()
    #t.translate(txt)
    #time.sleep(1)
    while True:
       t.translate(input("你要翻译啥:"),fromLang="en",toLang="zh")
        
