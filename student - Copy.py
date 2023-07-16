from cProfile import label
from importlib.resources import contents
from logging import root
from multiprocessing.sharedctypes import Value
from re import I
from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import update
from PIL import Image,ImageTk #pip install pillow
import mysql.connector
from tkinter import messagebox


class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")


        #variables
        self.var_cou=StringVar()
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_stu_id=StringVar()
        self.var_univ_id=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_father=StringVar()
        self.var_mobile=StringVar()
        self.var_sess=StringVar()
        self.var_quota=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()


        img=Image.open(r"photos\logo.png")
        img=img.resize((1365,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        self.btn_1=Button(self.root,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=1365,height=130)

        #background image
        img=Image.open(r"photos\logo-bg.png")
        img=img.resize((1365,600),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img)

        bg_lbl=Label(self.root,image=self.photoimg_2,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=130,width=1365,height=600)

        lbl_title = Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",32,"bold"),fg="brown",bg="yellow")
        lbl_title.place(x=30,y=5,width=1300,height=40)


        #manage frame
        Manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="yellow")
        Manage_frame.place(x=15,y=50,width=1325,height=510)


        #left frame
        DataLeftFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="brown",bg="white")
        DataLeftFrame.place(x=20,y=10,width=530,height=490)

        #current course label frame
        std_lbl_info_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Current Course Information",font=("times new roman",12,"italic"),fg="red",bg="white")
        std_lbl_info_frame.place(x=10,y=5,width=500,height=130)

        #labels course
        lbl_cou = Label(std_lbl_info_frame,text="Course:",font=("Times new roman",12,"bold"),bg="white")
        lbl_cou.grid(row=0,column=0,padx=2,sticky=W)

        comb_cour=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_cou,font=("times new roman",12,"normal"),width=15,state="readonly")
        comb_cour["value"]=("Select Course","B.Tech","BCA","BBA","MBA","M.Tech")
        comb_cour.current(0)
        comb_cour.grid(row=0,column=1,padx=2,pady=10,sticky=W)



        #labels deparment
        lbl_dep = Label(std_lbl_info_frame,text="Deparment:",font=("Times new roman",12,"bold"),bg="white")
        lbl_dep.grid(row=0,column=2,padx=2,sticky=W)

        comb_dep=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_dep,font=("times new roman",12,"normal"),width=15,state="readonly")
        comb_dep["value"]=("Select Department","CIVIL","CSE","IT","ECE","EEE","ME")
        comb_dep.current(0)
        comb_dep.grid(row=0,column=3,padx=2,pady=10,sticky=W)



        #labels Year
        lbl_yer = Label(std_lbl_info_frame,text="Year:",font=("Times new roman",12,"bold"),bg="white")
        lbl_yer.grid(row=1,column=0,padx=2,sticky=W)


        comb_yer=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_year,font=("times new roman",12,"normal"),width=15,state="readonly")
        comb_yer["value"]=("Select Year","First","Second","Third","Fourth")
        comb_yer.current(0)
        comb_yer.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #labels Semester
        lbl_sem = Label(std_lbl_info_frame,text="Semester:",font=("Times new roman",12,"bold"),bg="white")
        lbl_sem.grid(row=1,column=2,padx=2,sticky=W)

        comb_sem=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_sem,font=("times new roman",12,"normal"),width=15,state="readonly")
        comb_sem["value"]=("Select Semester","Ist sem","IInd sem")
        comb_sem.current(0)
        comb_sem.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #student class label frame
        std_lbl_class_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"italic"),fg="red",bg="white")
        std_lbl_class_frame.place(x=10,y=140,width=500,height=250)

        #labels
        #Student id 
        lbl_collid = Label(std_lbl_class_frame,text="Student Id:",font=("Times new roman",12,"bold"),bg="white")
        lbl_collid.grid(row=0,column=0,padx=2,sticky=W)

        id_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_stu_id,font=("Times new roman",12,"normal"),width=15)
        id_entry.grid(row=0,column=1,sticky=W,padx=2,pady=10)

         #university roll 
        lbl_uniid = Label(std_lbl_class_frame,text="University Id:",font=("Times new roman",12,"bold"),bg="white")
        lbl_uniid.grid(row=0,column=2,padx=2,sticky=W)

        uni_roll=ttk.Entry(std_lbl_class_frame,textvariable=self.var_univ_id,font=("Times new roman",12,"normal"),width=15)
        uni_roll.grid(row=0,column=3,sticky=W,padx=2,pady=10)

         #Name
        lbl_name = Label(std_lbl_class_frame,text="Name:",font=("Times new roman",12,"bold"),bg="white")
        lbl_name.grid(row=1,column=0,padx=2,sticky=W)

        name_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_name,font=("Times new roman",12,"normal"),width=15)
        name_entry.grid(row=1,column=1,sticky=W,padx=2,pady=10)

         #Date of birth 
        lbl_dob = Label(std_lbl_class_frame,text="D.O.B:",font=("Times new roman",12,"bold"),bg="white")
        lbl_dob.grid(row=1,column=2,padx=2,sticky=W)

        dob_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_dob,font=("Times new roman",12,"normal"),width=15)
        dob_entry.grid(row=1,column=3,sticky=W,padx=2,pady=10)

         #fathers name
        lbl_fatnm = Label(std_lbl_class_frame,text="Father Nm:",font=("Times new roman",12,"bold"),bg="white")
        lbl_fatnm.grid(row=2,column=0,padx=2,sticky=W)

        fatnm_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_father,font=("Times new roman",12,"normal"),width=15)
        fatnm_entry.grid(row=2,column=1,sticky=W,padx=2,pady=10)

         #mobile no 
        lbl_mobno = Label(std_lbl_class_frame,text="Mobile No.:",font=("Times new roman",12,"bold"),bg="white")
        lbl_mobno.grid(row=2,column=2,padx=2,sticky=W)

        mobno_en=ttk.Entry(std_lbl_class_frame,textvariable=self.var_mobile,font=("Times new roman",12,"normal"),width=15)
        mobno_en.grid(row=2,column=3,sticky=W,padx=2,pady=10)

         #session yr
        lbl_sesyr = Label(std_lbl_class_frame,text="Session yr:",font=("Times new roman",12,"bold"),bg="white")
        lbl_sesyr.grid(row=3,column=0,padx=2,sticky=W)

        ses_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_sess,font=("Times new roman",12,"normal"),width=15)
        ses_entry.grid(row=3,column=1,sticky=W,padx=2,pady=10)

         #Quota
        lbl_quota = Label(std_lbl_class_frame,text="Quota:",font=("Times new roman",12,"bold"),bg="white")
        lbl_quota.grid(row=3,column=2,padx=2,sticky=W)

        comb_quota=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_quota,font=("Times new roman",12,"normal"),width=13,state="readonly")
        comb_quota["value"]=("Select Quota","General","OBC","SC","ST")
        comb_quota.current(0)
        comb_quota.grid(row=3,column=3,padx=2,pady=10,sticky=W)

         #Email id
        lbl_email = Label(std_lbl_class_frame,text="Email.Id:",font=("Times new roman",12,"bold"),bg="white")
        lbl_email.grid(row=4,column=0,padx=2,sticky=W)

        email_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_email,font=("Times new roman",12,"normal"),width=15)
        email_entry.grid(row=4,column=1,sticky=W,padx=2,pady=10)

         #Address
        lbl_addr = Label(std_lbl_class_frame,text="Address:",font=("Times new roman",12,"bold"),bg="white")
        lbl_addr.grid(row=4,column=2,padx=2,sticky=W)

        add_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_address,font=("Times new roman",12,"normal"),width=15)
        add_entry.grid(row=4,column=3,sticky=W,padx=2,pady=10)

        #button frame
        btn_frame=Frame(DataLeftFrame,bd=4,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=400,width=500,height=40)

        btn_add=Button(btn_frame,text="Save",command=self.add_data,font=("Cooper Black",12,),width=10,bg="blue",fg="white",borderwidth=0)
        btn_add.grid(row=0,column=1,padx=3,pady=2)

        btn_update=Button(btn_frame,text="Update",command=self.update_data,font=("Cooper Black",12,),width=10,bg="blue",fg="white",borderwidth=0)
        btn_update.grid(row=0,column=2,padx=4,pady=2)

        btn_Remove=Button(btn_frame,text="Delete",command=self.delete_data,font=("Cooper Black",12,),width=10,bg="blue",fg="white",borderwidth=0)
        btn_Remove.grid(row=0,column=3,padx=4,pady=2)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset_data,font=("Cooper Black",12,),width=10,bg="blue",fg="white",borderwidth=0)
        btn_reset.grid(row=0,column=4,padx=4,pady=2)




        #right frame
        DataRightFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Database",font=("times new roman",12,"bold"),fg="brown",bg="white")
        DataRightFrame.place(x=560,y=10,width=745,height=490)

        #image
        img_right=Image.open(r"photos\head.jpg")
        img_right.resize((745,100),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img_right)

        my_img=Label(DataRightFrame,image=self.photoimg3,bd=3,relief=RIDGE)
        my_img.place(x=2,y=3,width=730,height=100)

        #search
        searchFrame=LabelFrame(DataRightFrame,bd=4,relief=RIDGE,padx=2,text="Search Student Information",font=("times new roman",12,"bold"),fg="brown",bg="white")
        searchFrame.place(x=0,y=105,width=730,height=65)

        Seach_by=Label(searchFrame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        Seach_by.grid(row=0,column=0,sticky=W,padx=5)

        #search by
        self.var_com_search=StringVar()
        search_by=ttk.Combobox(searchFrame,textvariable=self.var_com_search,font=("Times new roman",12,"normal"),width=13,state="readonly")
        search_by["value"]=("Select Option","Student_Id","University_Id","Mobile_no")
        search_by.current(0)
        search_by.grid(row=0,column=1,padx=5,sticky=W)

        self.var_search=StringVar()
        txt_search=ttk.Entry(searchFrame,textvariable=self.var_search,font=("Times new roman",12,"normal"),width=16)
        txt_search.grid(row=0,column=2,sticky=W,padx=5,pady=10)

        btn_Search=Button(searchFrame,command=self.search_data,text="Search",font=("Cooper Black",12,),width=14,bg="blue",fg="white",borderwidth=0)
        btn_Search.grid(row=0,column=3,padx=5)

        btn_ShowAll=Button(searchFrame,command=self.fetch_data,text="Show All",font=("Cooper Black",12,),width=14,bg="blue",fg="white",borderwidth=0)
        btn_ShowAll.grid(row=0,column=4,padx=5)

        #***********************Student Table and scroll bar ****************************
        table_frame=Frame(DataRightFrame,bd=4,relief=RIDGE,bg="white")
        table_frame.place(x=0,y=172,width=730,height=290)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("Course","Dep","Year","Sem","Stud id","Univ id","Name","DoB","Father","Mob.no","Ses","Quota","Email id","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Dep",text="Deparment")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Stud id",text="Student Id")
        self.student_table.heading("Univ id",text="University Id")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("DoB",text="D.O.B")
        self.student_table.heading("Father",text="Father Nm")
        self.student_table.heading("Mob.no",text="Mobile No.")
        self.student_table.heading("Ses",text="Session yr")
        self.student_table.heading("Quota",text="Quota")
        self.student_table.heading("Email id",text="Email .id")
        self.student_table.heading("Address",text="Address")

        self.student_table["show"]="headings"

        self.student_table.column("Course",width=100)
        self.student_table.column("Dep",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Stud id",width=100)
        self.student_table.column("Univ id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("DoB",width=100)
        self.student_table.column("Father",width=100)
        self.student_table.column("Mob.no",width=100)
        self.student_table.column("Ses",width=100)
        self.student_table.column("Quota",width=100)
        self.student_table.column("Email id",width=100)
        self.student_table.column("Address",width=180)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if(self.var_cou.get()=="" or self.var_dep.get()=="" or self.var_name.get()==""):
            messagebox.showerror("Error","All Fields Are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="rishabh",passwd="rishabh2000@",database="student1")
                my_curso=conn.cursor()
                my_curso.execute("insert into studentmanagment values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_cou.get(),
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_stu_id.get(),
                    self.var_univ_id.get(),
                    self.var_name.get(),
                    self.var_dob.get(),
                    self.var_father.get(),
                    self.var_mobile.get(),
                    self.var_sess.get(),
                    self.var_quota.get(),
                    self.var_email.get(),
                    self.var_address.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been added!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #fetch Function
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="rishabh",passwd="rishabh2000@",database="student1")
        my_curso=conn.cursor()
        my_curso.execute("select * from studentmanagment")
        data=my_curso.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get selected value
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]

        self.var_cou.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_stu_id.set(data[4]),
        self.var_univ_id.set(data[5]),
        self.var_name.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_father.set(data[8]),
        self.var_mobile.set(data[9]),
        self.var_sess.set(data[10]),
        self.var_quota.set(data[11]),
        self.var_address.set(data[13]),
        self.var_email.set(data[12]),

    #Update
    def update_data(self):
        if (self.var_dep.get()=="" or self.var_univ_id.get()=="" or self.var_name.get()==""):
            messagebox.showerror("Error","All Fields Are required")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure you want to update this student data",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",user="rishabh",passwd="rishabh2000@",database="student1")
                    my_curso=conn.cursor()
                    my_curso.execute("update studentmanagment set Course=%s,Dept=%s,Year=%s,Semester=%s,University_Id=%s,Name=%s,DoB=%s,Father=%s,Mobile_no=%s,Session=%s,Quota=%s,Email_id=%s,Address=%s where Student_Id=%s",(
                    self.var_cou.get(),
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_univ_id.get(),
                    self.var_name.get(),
                    self.var_dob.get(),
                    self.var_father.get(),
                    self.var_mobile.get(),
                    self.var_sess.get(),
                    self.var_quota.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_stu_id.get()  
                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success","Student successfully updaded",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #Delete function
    def delete_data(self):
        if self.var_stu_id.get()=="":
            messagebox.showerror("Error","All Fields Are required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are you sure to delete this data",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",user="rishabh",passwd="rishabh2000@",database="student1")
                    my_curso=conn.cursor()
                    sql="delete from studentmanagment where Student_Id=%s"
                    value=(self.var_stu_id.get(),)
                    my_curso.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Your student data has been deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    #Reset
    def reset_data(self):
        self.var_cou.set("Select Course"),
        self.var_dep.set("Select Deparment"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_stu_id.set(""),
        self.var_univ_id.set(""),
        self.var_name.set(""),
        self.var_dob.set(""),
        self.var_father.set(""),
        self.var_mobile.set(""),
        self.var_sess.set(""),
        self.var_quota.set("Select Quota"),
        self.var_address.set(""),
        self.var_email.set("")

    #Search by function
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search=="":
            messagebox.showerror("Error","Please select an option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="rishabh",passwd="rishabh2000@",database="student1")
                my_curso=conn.cursor()
                my_curso.execute("select * from studentmanagment where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_curso.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



 



               


if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()
     