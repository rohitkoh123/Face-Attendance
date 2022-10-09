from customtkinter import *
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1920x1200')
        self.root.title('Face Recoginition System')

        #Variables
        self.department = StringVar()
        self.course = StringVar()
        self.year = StringVar()
        self.semester = StringVar()
        self.studentID = StringVar()
        self.studentName = StringVar()
        self.studentPhone = StringVar()
        self.studentTeacher = StringVar()
        self.gender = StringVar()
        self.photo = StringVar()



        title1 = CTkLabel(root,text="Student")
        title1.pack()

        #Frame
        mainFrame = CTkFrame(root)
        mainFrame.place(x=20,y=50,width=1400,height=700)

        #LeftFrame
        leftFrame = LabelFrame(mainFrame,text = "Student Details",bg="dark grey")
        leftFrame.place(x=10,y=10,width=610,height=650)

        #Current Course
        currentCourseFrame = LabelFrame(leftFrame,text="Current Course",bg="dark grey")
        currentCourseFrame.place(x=12,y=24,width=580,height=120)

        

        #Combo box style
        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground= "orange", background= "white")

        #Department
        
        depLabel = Label(currentCourseFrame,text="Departmetnt",bg="dark grey")
        depLabel.grid(row=0,column=0,sticky=W,pady=20,padx=2)

        depCombo = ttk.Combobox(currentCourseFrame,state="readonly",textvariable=self.department)
        depCombo["values"] = ("Select Department","Computer Science","Mechanical")
        depCombo.current(0)
        depCombo.grid(row=0,column=1,sticky=W)
        
        #Course

        courseLabel = Label(currentCourseFrame,text="Course",bg="dark grey")
        courseLabel.grid(row=0,column=2,sticky=W)

        courseCombo = ttk.Combobox(currentCourseFrame,state="readonly",textvariable=self.course)
        courseCombo["values"] = ("Select Course","First Year","Second Year","Third Year","Fourth Year")
        courseCombo.current(0)
        courseCombo.grid(row=0,column=3,sticky=W)

        #Year


        yearLabel = Label(currentCourseFrame,text="Year",bg="dark grey")
        yearLabel.grid(row=1,column=0,sticky=W)

        yearCombo = ttk.Combobox(currentCourseFrame,state="readonly",textvariable=self.year)
        yearCombo["values"] = ("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        yearCombo.current(0)
        yearCombo.grid(row=1,column=1,padx=2,sticky=W)


        #Semester


        semesterLabel = Label(currentCourseFrame,text="Semester",bg="dark grey")
        semesterLabel.grid(row=1,column=2,sticky=W)

        semesterCombo = ttk.Combobox(currentCourseFrame,state="readonly",textvariable=self.semester)
        semesterCombo["values"] = ("Select Semester","First Semester","Second Semester","Third Semester","Fourth Semester","Fifth Semester","Sixth Semester","Seventh Semester","Eighth Semster")
        semesterCombo.current(0)
        semesterCombo.grid(row=1,column=3,padx=2,sticky=W)



        #Student Details Frame
        studentFrame = LabelFrame(leftFrame,text="Student Details",bg="dark grey")
        studentFrame.place(x=12,y=180,width=580,height=320)

        #student ID

        studentIDlabel = Label(studentFrame,text="Student ID",bg="dark grey")
        studentIDlabel.grid(row=0,column=0,padx=2,pady=20,sticky=W)

        studentIDentry= Entry(studentFrame,bg="dark grey",width=16,textvariable=self.studentID)
        studentIDentry.grid(row=0,column=1,sticky=W)

        # student Name

        studentNamelabel = Label(studentFrame,text="Student Name",bg="dark grey")
        studentNamelabel.grid(row=0,column=2,padx=2,pady=20,sticky=W)

        studentNameentry= Entry(studentFrame,bg="dark grey",width=16,textvariable=self.studentName)
        studentNameentry.grid(row=0,column=3,sticky=W)

        
        #Phone Number

        studentphonelabel = Label(studentFrame,text="Phone Number",bg="dark grey")
        studentphonelabel.grid(row=1,column=0,padx=2,pady=20,sticky=W)

        studentphoneentry= Entry(studentFrame,bg="dark grey",width=16,textvariable=self.studentPhone)
        studentphoneentry.grid(row=1,column=1,sticky=W)

        # Teacher

        studentTeacherlabel = Label(studentFrame,text="Teacher Name",bg="dark grey")
        studentTeacherlabel.grid(row=1,column=2,padx=2,pady=20,sticky=W)

        studentTeacherentry= Entry(studentFrame,bg="dark grey",width=16,textvariable=self.studentTeacher)
        studentTeacherentry.grid(row=1,column=3,sticky=W)

        #Gender
        
        studentGenderlabel = Label(studentFrame,text="Gender",bg="dark grey")
        studentGenderlabel.grid(row=2,column=0,sticky=W)

        MaleRadio = Radiobutton(studentFrame,text="Male",value="Male",variable=self.gender)
        MaleRadio.grid(row=2,column=1,sticky=W)

        FemaleRadio = Radiobutton(studentFrame,text="Female",value="Female",variable=self.gender)
        FemaleRadio.grid(row=2,column=2,sticky=W)


        btn1 = Radiobutton(studentFrame,text="Take photo sample",value="Yes",variable=self.photo)
        btn1.grid(row=3,column=0)

        btn2 = Radiobutton(studentFrame,text="No photo sample",value="No",variable=self.photo)
        btn2.grid(row=3,column=1)

        #Button Frame

        btnFrame = LabelFrame(leftFrame,text="Options",bg="dark grey")
        btnFrame.place(x=12,y=450,width=580,height=145)

        #Save button

        saveBtn = Button(btnFrame,text="Save",command=self.addData)
        saveBtn.grid(row=0,column=0,padx=3)

        #update

        updateBtn = Button(btnFrame,text="Update",command=self.updateData)
        updateBtn.grid(row=0,column=1,padx=3)

        #delete

        deleteBtn = Button(btnFrame,text="Delete",command=self.deleteData)
        deleteBtn.grid(row=0,column=2,padx=3)

        # Reset
        resetBtn = Button(btnFrame,text="Reset",command=self.resetData)
        resetBtn.grid(row=0,column=3,padx=3)

        #take photo btn

        photoBtn = Button(btnFrame,text="Take Photo",command=self.generateDataset)
        photoBtn.grid(row=0,column=4,padx=3)

        #update photo btn

        upphotoBtn = Button(btnFrame,text="Update Photo")
        upphotoBtn.grid(row=0,column=5,padx=3)

        #rightFrame
        rightFrame = LabelFrame(mainFrame,text = "Options",bg="dark grey")
        rightFrame.place(x=630,y=10,width=755,height=650)

        #Search System

        searchFrame = LabelFrame(rightFrame,text="Search",bg="dark grey")
        searchFrame.place(x=12,y=24,width=680,height=120)

        searchBarlabel = Label(searchFrame,text="Search Bar",bg="dark grey")
        searchBarlabel.grid(row=0,column=0,padx=2,pady=20,sticky=W)

        #Search Combo
                
        searchCombo = ttk.Combobox(searchFrame,state="readonly")
        searchCombo["values"] = ("Select","Roll No","Phone No")
        searchCombo.current(0)
        searchCombo.grid(row=0,column=1,sticky=W,padx=2)

        #SearchBar Entry
        
        Searchentry= Entry(searchFrame,bg="dark grey",width=18)
        Searchentry.grid(row=0,column=2,sticky=W,padx=2)

        #serach button

        searchBtn = Button(searchFrame,text="Search")
        searchBtn.grid(row=0,column=3,sticky = W,padx=2)

        #show button

        showAllBtn = Button(searchFrame,text="Show All")
        showAllBtn.grid(row=0,column=4,sticky = W)


        #Table Frame
        tableFrame = LabelFrame(rightFrame,text="Table ",bg="dark grey")
        tableFrame.place(x=12,y=150,width=680,height=460)

        scrollx=ttk.Scrollbar(tableFrame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(tableFrame,orient=VERTICAL)

        #Tree View
        self.studentTable=ttk.Treeview(tableFrame,column=("Dep","Course","Year","Sem","Id","Name","Phone","Teacher","Gender","Photo"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.studentTable.xview)
        scrolly.config(command=self.studentTable.yview)

        #Making Heading
        self.studentTable.heading("Dep",text="Department")
        self.studentTable.heading("Course",text="Course")
        self.studentTable.heading("Year",text="Year")
        self.studentTable.heading("Sem",text="Semester")
        self.studentTable.heading("Id",text="Student ID")
        self.studentTable.heading("Name",text="Student Name")
        self.studentTable.heading("Phone",text="Phone Number")
        self.studentTable.heading("Teacher",text="Teacher Name")
        self.studentTable.heading("Gender",text="Gender")
        self.studentTable.heading("Photo",text="Photo Status")
        self.studentTable["show"] = "headings"
        #Making width of colums
        self.studentTable.column("Dep",width=100)
        self.studentTable.column("Course",width=100)
        self.studentTable.column("Year",width=100)
        self.studentTable.column("Sem",width=100)
        self.studentTable.column("Id",width=100)
        self.studentTable.column("Name",width=100)
        self.studentTable.column("Phone",width=100)
        self.studentTable.column("Teacher",width=100)
        self.studentTable.column("Gender",width=100)
        self.studentTable.column("Photo",width=100)

        self.studentTable.pack(fill = BOTH,expand=1)
        self.studentTable.bind("<ButtonRelease>",self.getCursor)
        self.fetchData()
        

    #Functions for adding Data

    def addData (self):
        if self.department.get()=="Select Department" or self.studentName.get()=="" or self.studentID.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:

                #insert data
                conn = mysql.connector.connect(host="localhost",username="root",password="rohit@123",database="FaceAttendance")
                mycursor = conn.cursor()
                mycursor.execute("insert into studen values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                self.department.get(),
                self.course.get(), 
                self.year.get(), 
                self.semester.get(), 
                self.studentID.get(), 
                self.studentName.get(), 
                self.studentPhone.get(), 
                self.studentTeacher.get(), 
                self.gender.get(), 
                self.photo.get() )
                )
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("Success","Student Details have been added",parent=self.root)

            except Exception as es:
                messagebox.showerror("Eroor",f"Due to {str(es)}",parent=self.root)



    #Function to put data on our table

    def fetchData(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="rohit@123",database="FaceAttendance")
        mycursor = conn.cursor()
        mycursor.execute('select * from studen')
        data = mycursor.fetchall()

        if len(data)!=0:
            #making table empty before putting
            self.studentTable.delete(*self.studentTable.get_children())
            for i in data:
                self.studentTable.insert("",END,values=i)
            conn.commit()
        
        conn.close()

    #Function to show values after clicking    

    def getCursor(self,event=""):
        cursorFocus = self.studentTable.focus()
        content=self.studentTable.item(cursorFocus)
        data = content["values"]

        self.department.set(data[0]),
        self.course.set(data[1]), 
        self.year.set(data[2]), 
        self.semester.set(data[3]), 
        self.studentID.set(data[4]), 
        self.studentName.set(data[5]), 
        self.studentPhone.set(data[6]), 
        self.studentTeacher.set(data[7]), 
        self.gender.set(data[8]), 
        self.photo.set(data[9]) 

    #Functionality for update
    def updateData(self):

        if self.department.get()=="Select Department" or self.studentName.get()=="" or self.studentID.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update","Do you want to update details",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="rohit@123",database="FaceAttendance")
                    mycursor = conn.cursor()
                    mycursor.execute("Update studen set department = %s,Course=%s,Year=%s,Semester=%s,Name=%s,Phone=%s,Teacher=%s,Gender=%s,Photo=%s where studentID=%s",(
                    self.department.get(),
                    self.course.get(), 
                    self.year.get(), 
                    self.semester.get(), 
                    self.studentName.get(), 
                    self.studentPhone.get(), 
                    self.studentTeacher.get(), 
                    self.gender.get(), 
                    self.photo.get(), 
                    self.studentID.get() ))

                else:
                    if not update:
                        return 
                messagebox.showinfo("Success","Students details updated sucesfully",parent=self.root)        
                conn.commit()
                self.fetchData()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)    


    #Functionlidty delete
    def deleteData(self):
        if self.studentID.get()=="":
            messagebox.showerror("Error","Student Id must be required")
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="rohit@123",database="FaceAttendance")
                    mycursor = conn.cursor()
                    sql = 'delete from studen where studentid= %s'
                    val= (self.studentID.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student values",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)  

    #Reset button functionality
    def resetData(self):
        self.department.set("Select Department"),
        self.course.set("Select Course"), 
        self.year.set("Select Year"), 
        self.semester.set("Select Semester"), 
        self.studentID.set(""), 
        self.studentName.set(""), 
        self.studentPhone.set(""), 
        self.studentTeacher.set(""), 
        self.gender.set("Male"), 
        self.photo.set("No") 

    #Take photo sample
    def generateDataset(self):
        if self.department.get()=="Select Department" or self.studentName.get()=="" or self.studentID.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="rohit@123",database="FaceAttendance")
                mycursor = conn.cursor()
                mycursor.execute("select * from studen")
                myresult =mycursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1
                    mycursor.execute("Update studen set department = %s,Course=%s,Year=%s,Semester=%s,Name=%s,Phone=%s,Teacher=%s,Gender=%s,Photo=%s where studentID=%s",(
                    self.department.get(),
                    self.course.get(), 
                    self.year.get(), 
                    self.semester.get(), 
                    self.studentName.get(), 
                    self.studentPhone.get(), 
                    self.studentTeacher.get(), 
                    self.gender.get(), 
                    self.photo.get(), 
                    self.studentID.get()==id+1 ))
                
                conn.commit()
                self.fetchData()
                self.resetData()
                conn.close()

                #using predefined data 

                faceClassifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def faceCropped(img):
                    grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = faceClassifier.detectMultiScale(grayimg,1.3,5)

                    for (x,y,w,h) in faces:
                        faceCropped=img[y:y+h,x:x+w]
                        return faceCropped
                # 0- webcam
                capture = cv2.VideoCapture(0)
                imgid = 0
                while True:
                    ret,myframe = capture.read()
                    if faceCropped(myframe) is not None:
                        imgid+=1
                        face = cv2.resize(faceCropped(myframe),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        filePath = "data/name"+str(id)+"."+str(imgid)+".jpg"
                        cv2.imwrite(filePath,face)
                        cv2.putText(face,str(imgid),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(imgid) ==100:
                        break
                capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed")

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent = self.root)










        


        
       




        
        


if __name__=="__main__":
    root = CTk()
    Obj = Student(root)
    root.mainloop()      