import json
import requests
import time
from 人工智障识别语音 import BaiduASR,BaiduSpeech
from audio import Recorder,Player
#while True:
#    url = "https://api.ownthink.com/bot?spoken="
#    ask = input("接下来说什么...？:")
#    r = requests.get(url+ask)
#    print(r.text)
class XiaosiRobot:
    def __init__(self):
        self.appid = ""
        self.userid = ""
    def chat(self,spoken):
        url = "https://api.ownthink.com/bot"
        body = {"spoken":spoken,"appid":self.appid,"userid":self.userid}
        respond = requests.post(url,data = body)
        print(respond)
        r = respond.json()
        if r ["message"] == "success":
            data = r["data"]
            if data["type"] == 5000:
                text = data["info"]["text"]
                print(time.strftime("%Y-%m-%d %H:%M:%S:"),"Re:",text)
                return text
        else:
            print("No...")
            return "No..."
if __name__ == '__main__':
    robot = XiaosiRobot()
    fp = "test.wav"
    recorder = Recorder()
    recorder.record(fp)
    asr = BaiduASR()
    result = asr.transcrible(fp)
    speech = BaiduSpeech()
    player = Player()
    while True:
        text = robot.chat(result)
        fp = speech.get_speech(text)
        player.play(fp)
        recorder.record(fp)
        result = asr.transcrible(fp)
