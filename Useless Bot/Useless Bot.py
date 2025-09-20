import tkinter as tk
import tkinter.font as tf
from 人工智障识别语音 import BaiduSpeech,BaiduASR
from AI import XiaosiRobot
from audio import Player,Recorder
import threading
from 图像识别 import ImageClassify,Face
from camera import Camera
from 憨憨翻译 import Translate
class App():
    def __init__(self,root):
        self.root = root
        self.root.title('Useless bot-w-')
        self.root.geometry('960x540')
        self.state = False
        self.root.bind("<F11>",self.toggle_fullscreen)
        self.root.bind("<Escape>",self.end_fullscreen)
        MainFace(self.root)
    def toggle_fullscreen(self,event=None):
        self.state = not self.state
        self.root.attributes("-fullscreen",self.state)
    def end_fullscreen(self,event=None):
        self.state = False
        self.root.attributes("-fullscreen",False)
class MainFace():
    def __init__(self,root):
        self.root = root
        self.create_widget()
    def create_widget(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        lb1 = tk.Label(self.frame,text="Useless Bot-w-",font=tf24)
        lb1.grid(row=0,column=1,padx=20,pady=20)
        bt1 = tk.Button(self.frame,text="Recorder",font=tf18,command=self.luyinji)
        bt1.grid(row=1,column=0,padx=5,pady=5)
        bt2 = tk.Button(self.frame,text="Conversation",font=tf18,command=self.conversation)
        bt2.grid(row=1,column=2,padx=5,pady=5)
        lb3 = tk.Button(self.frame,text="Face Dectection",font=tf18,command=self.beauty)
        lb3.grid(row=2,column=0,padx=5,pady=5)
        bt4 = tk.Button(self.frame,text="Object Dectection",font=tf18,command=self.obj_detec)
        bt4.grid(row=2,column=2,padx=5,pady=5)
        lb5 = tk.Button(self.frame,text="NG",font=tf18,command=self.robot_move)
        lb5.grid(row=3,column=0,padx=5,pady=5)
        bt6 = tk.Button(self.frame,text="Translate",font=tf18,command=self.fanyi)
        bt6.grid(row=3,column=2,padx=5,pady=5)
    def luyinji(self):
        self.frame.destroy()
        Luyinji(self.root)
    def conversation(self):
        #pass
        self.frame.destroy()
        Conversation(self.root)
    def beauty(self):
        #pass
        self.frame.destroy()
        Beauty(self.root)
    def obj_detec(self):
        self.frame.destroy()
        ObjDetec(self.root)
    def robot_move(self):
        pass
    def fanyi(self):
        #pass
        self.frame.destroy()
        Fanyi(self.root)
class Luyinji:
    def __init__(self,root):
        self.root = root#窗口
        self.recorder = Recorder()#录音对象
        self.player = Player()#播放对象
        self.create_widget()#窗口布局
    def create_widget(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        tk.Label(self.frame,text="filename:",font=tf18).grid(row=0,column=0)
        self.entry1 = tk.Entry(self.frame,width=10,justify=tk.RIGHT,font=tf18)
        self.entry1.insert(0,"record")
        self.entry1.grid(row=0,column=1)
        tk.Label(self.frame,text="time:",font=tf18).grid(row=1,column=0)
        self.entry2 = tk.Entry(self.frame,width=10,justify=tk.RIGHT,font=tf18)
        self.entry2.insert(0,"5")
        self.entry2.grid(row=1,column=1)
        tk.Label(self.frame,text=".wav",font=tf18).grid(row=0,column=2) 
        tk.Label(self.frame,text="S",font=tf18).grid(row=1,column=2) 
        tk.Button(self.frame,text="Record",font=tf18,command=self.record).grid(row=3,column=0)
        tk.Button(self.frame,text="End",font=tf18,command=self.stop_record).grid(row=3,column=2)
        tk.Button(self.frame,text="Play",font=tf18,command=self.play).grid(row=4,column=0)
        tk.Button(self.frame,text="Stop",font=tf18,command=self.stop_play).grid(row=4,column=2)
        tk.Button(self.frame,text="Back",font=tf18,command=self.back).grid(row=5,column=1)
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
    def back(self):
        self.frame.destroy()
        MainFace(self.root)
class Conversation():
    def __init__(self,root):
        self.root = root
        self.running = False
        self.create_widget()
    def create_widget(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        tk.Label(self.frame,text="Conversation",font = tf24).grid(row=0,column=0,columnspan=2)
        self.quest = tk.StringVar()
        tk.Label(self.frame,textvariable=self.quest,
                 width=60,height=4,
                 wraplength=1000,
                 bg="white",
                 font=tf18).grid(row=1,column=0,columnspan=2)
        self.answer = tk.StringVar()
        tk.Label(self.frame,textvariable=self.answer,
                 width=60,height=6,
                 wraplength=800,
                 bg="white",
                 font=tf18).grid(row=2,column=0,columnspan=2)
        tk.Button(self.frame,text="Let's talk",font=tf18,
                  command=self.conversation_thread).grid(row=3,column=0)
        tk.Button(self.frame,text="Return",font=tf18,
                  command=self.back).grid(row=3,column=1)
    def conversation(self):
        self.quest.set("Speaking please")
        self.answer.set("")
        record_wav = Recorder().record("record.wav",3)
        self.quest.set("I'm listening...")
        asr_text = BaiduSpeech().transcrible(record_wav)
        self.quest.set(asr_text)
        self.answer.set("I'm thinking...")
        #self.answer.set(answer)
        answer = XiaosiRobot().chat(asr_text)
        tts_wav = BaiduSpeech().get_speech(answer)
        self.answer.set(answer)
        Player().play(tts_wav)
        self.running = False
    def conversation_thread(self):
        if not self.running:
            t = threading.Thread(target=self.conversation)
            t.daemon = True
            t.start()
            self.running = True
    def back(self):
        self.frame.destroy()
        MainFace(self.root)
class ObjDetec():
    def __init__(self,root):
        self.root = root
        self.running = False
        self.obj = ImageClassify()
        self.camera = Camera()
        self.create_widget()
    def create_widget(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        tk.Label(self.frame,text="Object Detection",font = tf24).grid(row=0,column=0,columnspan=2)
        self.can1 = tk.Canvas(self.frame,bg='white',width=600,height=400)
        self.can1.grid(row=1,column=0,columnspan=6)
        self.can2 = tk.Canvas(self.frame,bg='white',width=300,height=400)
        self.can2.grid(row=1,column=6,columnspan=3)
        self.v = tk.IntVar()
        self.v.set(1)
        r1=tk.Radiobutton(self.frame,text="General",variable=self.v,value=1,font=tf18)
        r1.grid(row=2,column=0)
        r2=tk.Radiobutton(self.frame,text="Animals",variable=self.v,value=2,font=tf18)
        r2.grid(row=2,column=1)
        r3=tk.Radiobutton(self.frame,text="Plants",variable=self.v,value=3,font=tf18)
        r3.grid(row=2,column=2)
        r4=tk.Radiobutton(self.frame,text="logo",variable=self.v,value=4,font=tf18)
        r4.grid(row=2,column=3)
        r5=tk.Radiobutton(self.frame,text="Car",variable=self.v,value=5,font=tf18)
        r5.grid(row=2,column=4)
        r6=tk.Radiobutton(self.frame,text="Current",variable=self.v,value=6,font=tf18)
        r6.grid(row=2,column=5)
        bt1 = tk.Button(self.frame,text="Start",font=tf18,command=self.open)
        bt1.grid(row=2,column=6,padx=10,pady=10)
        bt2 = tk.Button(self.frame,text="Let me see!",font=tf18,command=self.snap)
        bt2.grid(row=2,column=7,padx=10,pady=10)
        bt3 = tk.Button(self.frame,text="Return",font=tf18,command=self.back)
        bt3.grid(row=2,column=8,padx=10,pady=10)
    def open(self):
        if not self.running:
            self.running = True
            self.video()
    def video(self):
        if self.running:
            self.imtk = self.camera.get_tk_frame()
            if self.imtk:
                self.can1.create_image((300,200),image=self.imtk)
            self.root.after(10,self.video)
    def snap(self):
        if self.running:
            self.running = False
            self.camera.take_photo()
        choice = self.v.get()
        if choice == 1:
            res = self.obj.general_detec("photo.jpg")
        elif choice == 2:
            res = self.obj.animal_detec("photo.jpg")
        elif choice == 3:
            res = self.obj.plant_detec("photo.jpg")
        elif choice == 4:
            res = self.obj.logo_detec("photo.jpg")
        elif choice == 5:
            res = self.obj.car_detec("photo.jpg")
        elif choice == 6:
            res = self.obj.currency_detec("photo.jpg")
        res = ''.join(res)
        self.can2.delete('t')
        self.can2.create_text(150,200,font=tf15,text=res,tag='t')
    def back(self):
        self.frame.destroy()
        self.camera.cam.release()
        MainFace(self.root)
class Beauty():
    def __init__(self,root):
        self.root = root
        self.running = False
        self.beauty = Face()
        self.camera = Camera()
        self.create_widget()
    def create_widget(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        tk.Label(self.frame,text="Face Detection",font = tf24).grid(row=0,column=0,columnspan=2)
        self.can1 = tk.Canvas(self.frame,bg='white',width=600,height=400)
        self.can1.grid(row=1,column=0,columnspan=6)
        self.can2 = tk.Canvas(self.frame,bg='white',width=300,height=400)
        self.can2.grid(row=1,column=6,columnspan=3)
        bt1 = tk.Button(self.frame,text="Start",font=tf18,command=self.open)
        bt1.grid(row=2,column=3,padx=10,pady=10)
        bt2 = tk.Button(self.frame,text="Let me see!",font=tf18,command=self.snap)
        bt2.grid(row=2,column=4,padx=10,pady=10)
        bt3 = tk.Button(self.frame,text="Return",font=tf18,command=self.back)
        bt3.grid(row=2,column=5,padx=10,pady=10)
    def open(self):
        if not self.running:
            self.running = True
            self.video()
    def video(self):
        if self.running:
            self.imtk = self.camera.get_tk_frame()
            if self.imtk:
                self.can1.create_image((300,200),image=self.imtk)
            self.root.after(10,self.video)
    def snap(self):
        if self.running:
            self.running = False
            self.camera.take_photo()
        #res = self.beauty_detect("photo.jpg")
        #res = self.obj.general_detec("photo.jpg")
        res = self.beauty.face_detect("photo.jpg")
        res = ''.join(res)
        self.can2.delete('t')
        self.can2.create_text(150,200,font=tf15,text=res,tag='t')
    def back(self):
        self.frame.destroy()
        self.camera.cam.release()
        MainFace(self.root)
class Fanyi():
    def __init__(self,root):
        self.root = root
        self.running = False
        self.fanyi = Translate()
        self.create_widget()
    def create_widget(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        tk.Label(self.frame,text="Transtate",font = tf24).grid(row=0,column=0,columnspan=2)
        self.text1 = tk.Text(self.frame,font=tf15,height=5,width=40)
        self.text1.grid(row=1,column=0,columnspan=2)
        bt1 = tk.Button(self.frame,text="ZH to EN",font=tf18,command=self.zh_to_en)
        bt1.grid(row=2,column=0,padx=10,pady=10)
        bt2 = tk.Button(self.frame,text="EN to ZH",font=tf18,command=self.en_to_zh)
        bt2.grid(row=3,column=0,padx=10,pady=10)
        bt1 = tk.Button(self.frame,text="ZH to EN(By sound)",font=tf18,command=self.v_zh_to_en)
        bt1.grid(row=2,column=1,padx=10,pady=10)
        bt2 = tk.Button(self.frame,text="EN to ZH(By sound)",font=tf18,command=self.v_en_to_zh)
        bt2.grid(row=3,column=1,padx=10,pady=10)
        self.text2 = tk.Text(self.frame,font=tf15,height=5,width=40)
        self.text2.grid(row=4,column=0,columnspan=2)
        bt3 = tk.Button(self.frame,text="Return",font=tf18,command=self.back)
        bt3.grid(row=5,column=0,padx=10,pady=10)
    def zh_to_en(self):
        string = self.text1.get(0.0,tk.END)
        result = Translate().translate(string,'zh','en')
        self.text2.delete(0.0,tk.END)
        self.text2.insert(tk.END,result)
    def en_to_zh(self):
        string = self.text1.get(0.0,tk.END)
        result = Translate().translate(string,'en','zh')
        self.text2.delete(0.0,tk.END)
        self.text2.insert(tk.END,result)
    def trans(self,fromlang,tolang):
        self.text1.delete(0.0,tk.END)
        self.text2.delete(0.0,tk.END)
        record_wav = Recorder().record("record.wav",1)
        asr_text = BaiduSpeech().transcrible(record_wav)
        if asr_text:
            self.text1.insert(tk.END,asr_text)
            result = Translate().translate(asr_text,fromlang,tolang)
            self.text2.delete(0.0,tk.END)
            self.text2.insert(tk.END,result)
        else:
            self.text1.insert(tk.END,"hmmmmm...?") 
    def v_zh_to_en(self):
        t = threading.Thread(target=self.trans,args=("zh","en"))
        t.daemon = True
        t.start()
    def v_en_to_zh(self):
        t = threading.Thread(target=self.trans,args=("en","zh"))
        t.daemon = True
        t.start()
    def back(self):
        self.frame.destroy()
        MainFace(self.root)
if __name__ == '__main__':
    root = tk.Tk()
    tf15 = tf.Font(family="微软雅黑",size=15)
    tf18 = tf.Font(family="微软雅黑",size=18)
    tf24 = tf.Font(family="微软雅黑",size=24)
    App(root)
    root.mainloop()
#root = tk.Tk()
#root.title("人工智障V1.0")
