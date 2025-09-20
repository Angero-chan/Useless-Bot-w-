import pyaudio
import wave
import time
class Player:
    def __init__(self):
        self.playing = False
        self.p = pyaudio.PyAudio()
    def play(self,filename):
        def callback(in_data,frame_count,time_info,status):
            data = wf.readframes(frame_count)
            return data,pyaudio.paContinue
        print(time.strftime("%Y-%m-%d %H:%M:%S"),"Playing...:",filename)
        self.playing = True
        wf = wave.open(filename,"rb")
        #p = pyaudio.PyAudio()
        stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()),channels=wf.getnchannels(),rate=wf.getframerate(),output=True,stream_callback=callback)
        while stream.is_active() and self.playing:
            time.sleep(0.1)
        stream.close()
        wf.close()
        self.playing = False
        print(time.strftime("%Y-%m-%d %H:%M:%S"),"Done!:",filename)
    def stop(self):
        self.playing = False
    def is_playing(self):
        return self.playing
if __name__ == '__main__':
    p = Player()
    p.play("test.wav")
