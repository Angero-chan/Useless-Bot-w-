import pyaudio
import wave
import time
class Recorder:
    def __init__(self):
        self.format = pyaudio.paInt16
        self.channels = 1
        self.width = 2
        self.rate = 16000
        self.recording = False
        self.p = pyaudio.PyAudio()
    def record(self,filename,t=5):
        def callback(in_data,frame_count,time_info,status):
            frames.append(in_data)
            return in_data,pyaudio.paContinue
        print(time.strftime("%Y-%m-%d %H:%M:%S"),"Recording...：",filename)
        self.recording = True
        frames = []
        stream = self.p.open(format=self.format,channels=self.channels,rate=self.rate,input=True,stream_callback=callback)
        for i in range(t*1000):
            time.sleep(0.001)
            if not self.recording:
                break
        stream.close()
        wf = wave.open(filename,'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.width)
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        self.recording = False
        print(time.strftime("%Y-%m-%d %H:%M:%S"),"Done!：",filename)
        return filename
    def stop(self):
        self.recording = False
    def is_recording(self):
        return self.recording
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
    r = Recorder()
    r.record("test.wav")
    p = Player()
    p.play("test.wav")
