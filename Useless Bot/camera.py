import cv2,tkinter
from PIL import Image,ImageTk
x = 0
class Camera():
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.photo = None
    def get_tk_frame(self):
        ret,frame = self.cam.read()
        if ret:
            self.photo = frame
            im_tk = self.img2tk(frame)
            return im_tk
    def take_photo(self):
        cv2.imwrite('photo.jpg',self.photo)
        return self.img2tk(self.photo)
    def img2tk(self,frame):
        img_flip = cv2.flip(frame,1)
        cv2image = cv2.cvtColor(img_flip,cv2.COLOR_BGR2RGBA)
        current_image = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(current_image)
        return imgtk
if __name__ == '__main__':
    root = tkinter.Tk()
    camera = Camera()
    while True:
        if camera.get_tk_frame():
            cv2.imshow("pic",camera.photo)
            cv2.waitKey(1)
        if cv2.waitKey(24) & 0xFF == ord('q'):
            x += 1
            if x > 1000//24:
                break
    camera.cam.release()
    cv2.destroyAllWindows()

