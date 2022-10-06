from customtkinter import *
# from tkinter import*
from tkinter import Label, ttk
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


        title1 = CTkLabel(root,text="Face Recogintion System")
        title1.pack()
        # Button Student Details
        b1 = CTkButton(root,text="Student Details")
        b1.pack()

        # Button Face Detector

        b2 = CTkButton(root,text="Face Detector")
        b2.pack()

        # Attendance
        b3 = CTkButton(root,text="Attendance")
        b3.pack()

        # Help Desk

        b4 = CTkButton(root,text="Help Desk")
        b4.pack()

        #Train Data
        b5 = CTkButton(root,text="Train Data")
        b5.pack()
        
        #Photos
        b6 = CTkButton(root,text="Photos")
        b6.pack()

        #Developer
        b7 = CTkButton(root,text="Developer")
        b7.pack()
        
    



#To check which file is running

if __name__ == "__main__":
    #Basic making root Object
    root = CTk()
    obj = FaceSystem(root)
    root.mainloop()