from customtkinter import *
# from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class FaceSystem:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1920x1200')
        self.root.title('Face Recoginition System')

        #First Image
        #To put image open(location)
        #img1 = Image.open()
        #Resizing and removing defects from image due to high level image to low
        #img1 = img1.resize((500,300),Image.ANTIALIAS)
        #self.photoimg1=ImageTk.PhotoImage(img1)

        #firstImg = Label(self.root,image=self.photoimg)
        #firstImg.place(x=0,y=0,width=500,height=300)



#To check which file is running

if __name__ == "__main__":
    #Basic making root Object
    root = CTk()
    obj = FaceSystem(root)
    root.mainloop()