from aip import AipSpeech
from audio import Recorder,Player
import time,wave
class BaiduASR():
    def __init__(self):
        appid = '25001878'#需改
        api_key = 'fSKCrDGyTpxF5W90IL2IEwFP'#需改
        secret_key = 'Eg55NLmu7I9NcPEFU5Kw2mUbXyUdI1tv'#需改
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
            #print(res)
            return ('')
class BaiduSpeech():
    def __init__(self):
        appid = '25001878'#需改
        api_key = 'fSKCrDGyTpxF5W90IL2IEwFP'#需改
        secret_key = 'Eg55NLmu7I9NcPEFU5Kw2mUbXyUdI1tv'#需改
        self.client = AipSpeech(appid,api_key,secret_key)
        self.dev_pid = 1536
        self.per = 0
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
            return ''
    def get_speech(self,tex):
        result = self.client.synthesis(tex,"zh",1,{'per':self.per,'aue':6})
        if not isinstance(result,dict):
            filepath = self.write_wav_file(result)
            ctime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
            print(ctime,"Done!:",result)
            return filepath
        else:
            print("...?")
    def write_wav_file(self,data):
        filepath = "temp_tts.wav"
        wf = wave.open(filepath,'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(16000)
        wf.writeframes(data)
        return filepath
        
if __name__ == "__main__":
    speech = BaiduSpeech()
    fp = speech.get_speech("今天是个上坟的好日子")
    player = Player()
    player.play(fp)
    fp = "test.wav"
    recorder = Recorder()
    recorder.record(fp)
    asr = BaiduASR()
    asr.transcrible(fp)
