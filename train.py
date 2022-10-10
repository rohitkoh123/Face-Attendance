from tkinter import*
from tkinter import Label, ttk
from PIL import Image,ImageTk
from student import Student
import os
import numpy as np
import cv2
from tkinter import messagebox



class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1920x1200')
        self.root.title('Train Data System')

        title1 = Label(self.root,text="Train Data Set")
        title1.pack()

        b1_btn = Button(self.root,text="Train Data",command=self.TrainClassifier)
        b1_btn.pack() 

    def TrainClassifier(self):
        dataFolder = "Data"
        pathF = [os.path.join(dataFolder,file) for file in os.listdir(dataFolder)]

        faces = []
        ids =[]

        for image in pathF:
            img = Image.open(image).convert('L') # image convert to grayscale for lbph
        #convert in grid
            imgGrid = np.array(img,'uint8')  # uint9 --> data type 
            idsplit = int(os.path.split(image)[1].split('.')[1]) #getting the id of image 

            faces.append(imgGrid)
            ids.append(idsplit)
            cv2.imshow("Training",imgGrid)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        #Train the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed!!")




if __name__ == "__main__":
    #Basic making root Object
    root = Tk()
    obj = Train(root)
    root.mainloop()