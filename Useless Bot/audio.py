import threading
import tkinter as tk
from recorder import Player,Recorder
class audio:
    def __init__(self,root):
        self.root = root#窗口
        self.recorder = Recorder()#录音对象
        self.player = Player()#播放对象
        self.create_widget()#窗口布局
    def create_widget(self):
        frame = tk.Frame(self.root)
        frame.pack()
        tk.Label(frame,text="filename:").grid(row=0,column=0)
        self.entry1 = tk.Entry(frame,width=10,justify=tk.RIGHT)
        self.entry1.insert(0,"record")
        self.entry1.grid(row=0,column=1)
        tk.Label(frame,text="time:").grid(row=1,column=0)
        self.entry2 = tk.Entry(frame,width=10,justify=tk.RIGHT)
        self.entry2.insert(0,"5")
        self.entry2.grid(row=1,column=1)
        tk.Label(frame,text=".wav").grid(row=0,column=2) 
        tk.Label(frame,text="S").grid(row=1,column=2) 
        tk.Button(frame,text="Record",command=self.record).grid(row=3,column=0)
        tk.Button(frame,text="End",command=self.stop_record).grid(row=3,column=1)
        tk.Button(frame,text="Play",command=self.play).grid(row=4,column=0)
        tk.Button(frame,text="Stop",command=self.stop_play).grid(row=4,column=1)
    def record(self):
        self.stop_record()#先停止录音
        name = self.entry1.get()
        name += ".wav"
        during = int(self.entry2.get())
        t = threading.Thread(target=self.recorder.record,args=(name,during))#多线程录音对象record
        t.daemon = True#线程守护设为真
        t.start()
    def stop_record(self):
        self.recorder.stop()
    def play(self):
        self.stop_play()
        name = self.entry1.get()
        name += ".wav"
        t = threading.Thread(target=self.player.play,args=(name,))
        t.daemon = True
        t.start()
    def stop_play(self):
        self.player.stop()

if __name__ =='__main__':
    root = tk.Tk()
    audio(root)#创建录音机对象
    root.mainloop()
