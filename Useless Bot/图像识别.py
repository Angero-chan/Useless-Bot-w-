import wave
import base64
from aip import AipSpeech,AipFace,AipImageClassify
import time
appid,api_key,secret_key = open("人脸识别appid.txt ").read().split()
class ImageClassify():
    def __init__(self):
        self.client = AipImageClassify(appid,api_key,secret_key)
    def general_detec(self,imagefile):
        image = open(imagefile,"rb").read()
        try:
            res = self.client.advancedGeneral(image)
            res = res["result"]
            detec = []
            for r in res:
                name = r["keyword"]
                score = f"{r['score']*100:.2f}%"
                detec.append(f"{res.index(r)+1}:{name} Similarity:{score}\n")
            return detec
        except:
            return "I can't understand this qwq"
    def animal_detec(self,imagefile):
        image = open(imagefile,"rb").read()
        try:
            res = self.client.animalDetect(image)
            #print(res)
            res = res["result"]
            detec = []
            for r in res:
                name = r["name"]
                score = f"{float(r['score'])*100:.2f}%"
                detec.append(f"{res.index(r)+1}:{name} Similarity:{score}\n")
            return detec
        except:
            return "I can't understand this qwq"

    def plant_detec(self,imagefile):
        image = open(imagefile,"rb").read()
        try:
            res = self.client.plantDetect(image)
            #print(res)
            res = res["result"]
            detec = []
            for r in res:
                name = r["name"]
                score = f"{float(r['score'])*100:.2f}%"
                detec.append(f"{res.index(r)+1}:{name} Similarity:{score}\n")
            return detec
        except:
            return "I can't understand this qwq"
    def currency_detec(self,imagefile):
        image = open(imagefile,"rb").read()
        try:
            res = self.client.currency(image)
            #print(res)
            res = res["result"]
            detec = []
            面值 = res["currencyDenomination"]
            货币名称 = res["currencyName"]
            年份 = res["year"]
            #RMB = f"{float(r['score'])*100:.2f}%"
            detec.append(f"{年份}:Value{面值},{货币名称}")
            return detec
        except:
            return "I can't understand this qwq"
    def logo_detec(self,imagefile):
        image = open(imagefile,"rb").read()
        try:
            res = self.client.logoSearch(image)
            #print(res)
            res = res["result"]
            detec = []
            for r in res:
                name = r["name"]
                score = f"{(r['probability'])*100:.2f}%"
                detec.append(f"{res.index(r)+1}:{name} Similarity:{score}\n")
            return detec
        except:
            return "I can't understand this qwq"
    def car_detec(self,imagefile):
        image = open(imagefile,"rb").read()
        try:
            res = self.client.carDetect(image)
            #print(res)
            res = res["result"]
            detec = []
            for r in res:
                name = r["name"]
                score = f"{(r['score'])*100:.2f}%"
                detec.append(f"{res.index(r)+1}:{name} Similarity:{score}\n")
            return detec
        except:
            return "What car is it?@w@"
    def ingredient_detec(self,imagefile):
        image = open(imagefile,"rb").read()
        try:
            res = self.client.ingredient(image)
            #print(res)
            res = res["result"]
            detec = []
            for r in res:
                name = r["name"]
                score = f"{(r['score'])*100:.2f}%"
                detec.append(f"{res.index(r)+1}:{name} Similarity:{score}\n")
            return detec
        except:
            return "Can I taste it?owo"
class BaiduASR():
    def __init__(self):
        self.client = AipSpeech(appid,api_key,secret_key)
        self.dev_pid = 1537
    def transcrible(self,fp):
        wav = open(fp,"rb").read()
        res = self.client.asr(wav,'pcm',16000,{'dev_pid' : self.dev_pid,})
        if res['err_no'] == 0:
            result = ''.join(res['result'])
            ctime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
            print(ctime,"Done!:",result)
            return result
        else:
            print(res)
            return str(res)
class BaiduSpeech():
    def __init__(self):
        self.client = AipSpeech(appid,api_key,secret_key)
        self.dev_pid = 1536
        self.per = 4
    def get_speech(self,tex):
        result = self.client.synthesis(tex,"zh",1,{'per':self.per,'aue':6})
        if not isinstance(result,dict):
            filepath = self.write_wav_file(result)
            ctime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
            print(ctime,"Done!:",result)
            return filepath
        else:
            print("What...")
    def write_wav_file(self,data):
        filepath = "temp_tts.wav"
        wf = wave.open(filepath,'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(16000)
        wf.writeframes(data)
        return filepath
class Face():
    def __init__(self):
        self.client = AipFace(appid,api_key,secret_key)
    def face_detect(self,imagefile):
        image = base64.b64encode(open(imagefile,'rb').read()).decode('utf-8')
        imageType = "BASE64"
        options = {"face_field":"beauty,age,gender,emotion"}
        result = self.client.detect(image,imageType,options)
        print(result)
        if result["error_code"] == 0:
            if result['result']['face_num']>0:
                age = result['result']['face_list'][0]["age"]
                beauty = result['result']['face_list'][0]["beauty"]
                gender = result['result']['face_list'][0]["gender"]["type"]
                gender = "♂" if gender == "male" else "♀"
                emotion = result['result']['face_list'][0]["emotion"]["type"]
                d = {"angry":"Angry xwx","disgust":"Disgust =w=","fear":"Fear qwq","happy":"Delighted awa","sad":"Sorrow qnq","surprise":"Surprise OAO","neutral":"Neutral -w-"}
                emotion = d[emotion]
                return f"Age: {age}\nBeauty:{beauty}\nGender:{gender}\nEmotion:{emotion}"
        else:
            print(result['error_code'])
            return rusult['err_msg']
if __name__ == '__main__':
    classify = ImageClassify()
    file = "gs.jfif"
    print(classify.ingredient_detec(file))
    file = "car6.png"
    print(classify.car_detec(file))
    file = "du.jfif"
    print(classify.logo_detec(file))
    #file = "money.jfif"
    #print(classify.currency_detec(file))
    #file = "grass2.webp"
    #print(classify.plant_detec(file))
    #file = "CAT.webp"
    #print(classify.animal_detec(file))
    #file = "福尔摩斯.png"
    #print(classify.general_detec(file))
    #face = Face()
    #while True:
    #    x = input("宁要搜什么图？:")
    #    r = face.face_detect(x)
    #    print(r)
