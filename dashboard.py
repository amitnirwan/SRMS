from tkinter import *
from PIL import Image,ImageTk  #pip install pillow
from course import CourseClass
from student import StudentClass
from Result import ResultClass
from report import reportClass

class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="white")





#icons

        self.logo_dash=ImageTk.PhotoImage(file="images/python_logo.png")




#title
        title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash, font=("goudy old style", 20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)


#Menu

        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1510,height=80)


        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white", cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="Students",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white", cursor="hand2",command=self.add_Student).place(x=260,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white", cursor="hand2",command=self.add_Result).place(x=500,y=5,width=200,height=40)
        btn_viewstudentsresult=Button(M_Frame,text="View Students Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white", cursor="hand2",command=self.add_report).place(x=760,y=5,width=200,height=40)
        btn_Logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white", cursor="hand2").place(x=1010,y=5,width=200,height=40)
        btn_Exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white", cursor="hand2").place(x=1280,y=5,width=200,height=40)


#content_window

        self.bg_img=Image.open("images/windows-10-lockscreen.png")
        self.bg_img=self.bg_img.resize((920,460),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=500,y=200,width=920,height=460)


#update Details

        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=500,y=680,width=300,height=100)

        self.lbl_students=Label(self.root,text="Total Students\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_students.place(x=810,y=680,width=300,height=100)

        self.lbl_result=Label(self.root,text="Total Result\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1120,y=680,width=300,height=100)





#Footer
        footer=Label(self.root,text="SRMS-Student Result Management System\nContact Us For any Technical Issue: 817xxxxx61", font=("goudy old style", 15),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)




    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)


    def add_Student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)



    def add_Result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win)


    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()