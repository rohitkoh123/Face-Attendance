from customtkinter import *
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1920x1200')
        self.root.title('Face Recoginition System')

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

        depCombo = ttk.Combobox(currentCourseFrame,state="readonly")
        depCombo["values"] = ("Select Department","Computer Science","Mechanical")
        depCombo.current(0)
        depCombo.grid(row=0,column=1,sticky=W)
        
        #Course

        courseLabel = Label(currentCourseFrame,text="Course",bg="dark grey")
        courseLabel.grid(row=0,column=2,sticky=W)

        courseCombo = ttk.Combobox(currentCourseFrame,state="readonly")
        courseCombo["values"] = ("Select Course","First Year","Second Year","Third Year","Fourth Year")
        courseCombo.current(0)
        courseCombo.grid(row=0,column=3,sticky=W)

        #Year


        yearLabel = Label(currentCourseFrame,text="Year",bg="dark grey")
        yearLabel.grid(row=1,column=0,sticky=W)

        yearCombo = ttk.Combobox(currentCourseFrame,state="readonly")
        yearCombo["values"] = ("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        yearCombo.current(0)
        yearCombo.grid(row=1,column=1,padx=2,sticky=W)


        #Semester


        semesterLabel = Label(currentCourseFrame,text="Semester",bg="dark grey")
        semesterLabel.grid(row=1,column=2,sticky=W)

        semesterCombo = ttk.Combobox(currentCourseFrame,state="readonly")
        semesterCombo["values"] = ("Select Semester","First Semester","Second Semester","Third Semester","Fourth Semester")
        semesterCombo.current(0)
        semesterCombo.grid(row=1,column=3,padx=2,sticky=W)



        #Student Details Frame
        studentFrame = LabelFrame(leftFrame,text="Student Details",bg="dark grey")
        studentFrame.place(x=12,y=180,width=580,height=320)

        #student ID

        studentIDlabel = Label(studentFrame,text="Student ID",bg="dark grey")
        studentIDlabel.grid(row=0,column=0,padx=2,pady=20,sticky=W)

        studentIDentry= Entry(studentFrame,bg="dark grey",width=16)
        studentIDentry.grid(row=0,column=1,sticky=W)

        # student Name

        studentNamelabel = Label(studentFrame,text="Student Name",bg="dark grey")
        studentNamelabel.grid(row=0,column=2,padx=2,pady=20,sticky=W)

        studentNameentry= Entry(studentFrame,bg="dark grey",width=16)
        studentNameentry.grid(row=0,column=3,sticky=W)

        
        #Phone Number

        studentphonelabel = Label(studentFrame,text="Phone Number",bg="dark grey")
        studentphonelabel.grid(row=1,column=0,padx=2,pady=20,sticky=W)

        studentphoneentry= Entry(studentFrame,bg="dark grey",width=16)
        studentphoneentry.grid(row=1,column=1,sticky=W)

        # Teacher

        studentTeacherlabel = Label(studentFrame,text="Teacher Name",bg="dark grey")
        studentTeacherlabel.grid(row=1,column=2,padx=2,pady=20,sticky=W)

        studentTeacherentry= Entry(studentFrame,bg="dark grey",width=16)
        studentTeacherentry.grid(row=1,column=3,sticky=W)

        #Gender
        gender =StringVar()
        studentGenderlabel = Label(studentFrame,text="Gender",bg="dark grey")
        studentGenderlabel.grid(row=2,column=0,sticky=W)

        MaleRadio = Radiobutton(studentFrame,variable=gender,text="Male",value="Male")
        MaleRadio.grid(row=2,column=1,sticky=W)

        FemaleRadio = Radiobutton(studentFrame,variable=gender,text="Female",value="Female")
        FemaleRadio.grid(row=2,column=2,sticky=W)


        btn1 = Radiobutton(studentFrame,text="Take photo sample",value="Yes")
        btn1.grid(row=3,column=0)

        btn2 = Radiobutton(studentFrame,text="No photo sample",value="Yes")
        btn2.grid(row=3,column=1)

        #Button Frame

        btnFrame = LabelFrame(leftFrame,text="Options",bg="dark grey")
        btnFrame.place(x=12,y=450,width=580,height=145)

        #Save button

        saveBtn = Button(btnFrame,text="Save")
        saveBtn.grid(row=0,column=0,padx=3)

        #update

        updateBtn = Button(btnFrame,text="Update")
        updateBtn.grid(row=0,column=1,padx=3)

        #delete

        deleteBtn = Button(btnFrame,text="Delete")
        deleteBtn.grid(row=0,column=2,padx=3)

        # Reset
        resetBtn = Button(btnFrame,text="Reset")
        resetBtn.grid(row=0,column=3,padx=3)

        #take photo btn

        photoBtn = Button(btnFrame,text="Take Photo")
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
        







        


        
       




        
        


if __name__=="__main__":
    root = CTk()
    Obj = Student(root)
    root.mainloop()      