# The Cust_Win class creates a GUI for adding customer details to a hotel management system using
# tkinter and mysql.connector.
from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


        #===================Variables==============
        self.var_ref=StringVar()
        x=random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()




        # =================Title=====================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)        


        # =============LOGO=====================
        img2=Image.open(r"E:\hms\hotel\logohotel.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)        

        #===============LABEL FRAME===============
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("arial",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #===============Label and Entry==========
#cust Ref
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"),state="readonly")   #ttk used for stylish 
        entry_ref.grid(row=0,column=1)

#cust name
        cname=Label(labelframeleft,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("arial",13,"bold")) 
        txtcname.grid(row=1,column=1)

#Mother name
        lblmname=Label(labelframeleft,text="Mother Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,width=29,font=("arial",13,"bold"))   #ttk used for stylish 
        txtmname.grid(row=2,column=1)

#Gender Combobox
        lbl_gender=Label(labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)
        
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")   #state used for text disabled in the box
        combo_gender["value"]=("male","Female","other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

#post code
        lblpostcode=Label(labelframeleft,text="PostCode:",font=("arial",12,"bold"),padx=2,pady=6)
        lblpostcode.grid(row=4,column=0,sticky=W)
        txtpostcode=ttk.Entry(labelframeleft,textvariable=self.var_post,width=29,font=("arial",13,"bold"))   #ttk used for stylish 
        txtpostcode.grid(row=4,column=1)

#mobile number
        lblmobile=Label(labelframeleft,text="Mobile:",font=("arial",12,"bold"),padx=2,pady=6)
        lblmobile.grid(row=5,column=0,sticky=W)
        txtmobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("arial",13,"bold"))   #ttk used for stylish 
        txtmobile.grid(row=5,column=1)

#email
        lblemail=Label(labelframeleft,text="Email:",font=("arial",12,"bold"),padx=2,pady=6)
        lblemail.grid(row=6,column=0,sticky=W)
        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("arial",13,"bold"))   #ttk used for stylish 
        txtemail.grid(row=6,column=1)

#nationality
        lblNationality=Label(labelframeleft,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")   #state used for text disabled in the box
        combo_Nationality["value"]=("Indian","USA","other")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)

#IdProof
        lblIdProof=Label(labelframeleft,text="Id Proof Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="readonly")   
        combo_id["value"]=("AdharCard","DrivingLicence","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)        

#id number
        lblIdnumber=Label(labelframeleft,text="Id Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdnumber.grid(row=9,column=0,sticky=W)
        txtIdnumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=29,font=("arial",13,"bold"))   #ttk used for stylish 
        txtIdnumber.grid(row=9,column=1)

#address
        lbladdress=Label(labelframeleft,text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
        lbladdress.grid(row=10,column=0,sticky=W)
        txtaddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("arial",13,"bold"))    
        txtaddress.grid(row=10,column=1)

        #================Btns=======================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #=======================Table Frame Search system=========================

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and search system",font=("arial",12,"bold"),padx=2,)
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_Frame,text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.serch_var=StringVar()
        combo_Serach=ttk.Combobox(Table_Frame,textvariable=self.serch_var,font=("arial",12,"bold"),width=24,state="readonly")   
        combo_Serach["value"]=("Mobile","Ref")
        combo_Serach.current(0)
        combo_Serach.grid(row=0,column=1,padx=2)      

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)


        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #======================Show Data Table=====================
        
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_details_Table.xview)
        scroll_y.config(command=self.Cust_details_Table.yview)

        self.Cust_details_Table.heading("ref",text="Refer No")
        self.Cust_details_Table.heading("name",text="Name")
        self.Cust_details_Table.heading("mother",text="Mother Name")
        self.Cust_details_Table.heading("gender",text="Gender")        
        self.Cust_details_Table.heading("post",text="PostCode")
        self.Cust_details_Table.heading("mobile",text="Mobile")
        self.Cust_details_Table.heading("email",text="Email")
        self.Cust_details_Table.heading("nationality",text="Nationality")
        self.Cust_details_Table.heading("idproof",text="Id Proof")
        self.Cust_details_Table.heading("idnumber",text="Id Number")
        self.Cust_details_Table.heading("address",text="Address")

        self.Cust_details_Table["show"]="headings"

        self.Cust_details_Table.column("ref",width=100)
        self.Cust_details_Table.column("name",width=100)
        self.Cust_details_Table.column("mother",width=100)
        self.Cust_details_Table.column("gender",width=100)
        self.Cust_details_Table.column("post",width=100)
        self.Cust_details_Table.column("mobile",width=100)
        self.Cust_details_Table.column("email",width=100)
        self.Cust_details_Table.column("nationality",width=100)        
        self.Cust_details_Table.column("idproof",width=100)
        self.Cust_details_Table.column("idnumber",width=100)
        self.Cust_details_Table.column("address",width=100)

        self.Cust_details_Table.pack(fill=BOTH,expand=1)
        self.Cust_details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

# =================ADD DATA================

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
                try:
                        conn=mysql.connector.connect(host="localhost",user="root",password="Bansal@2021",database="hms")
                        my_cursor=conn.cursor()
                        sql="insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        
                        data=(self.var_ref.get(), self.var_cust_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_id_proof.get(),self.var_id_number.get(),self.var_address.get())
                        my_cursor.execute(sql,data)
                        conn.commit()
                        self.fetch_data()
                        conn.close()                                                    
                        messagebox.showinfo("sucess","customer has been added",parent=self.root)
                except  Exception as es:                                                      
                        messagebox.showwarning("warning",f"something went to wrong:{str(es)}",parent=self.root)

# ====================FETCH DATA==================

    def fetch_data(self):          #This function fetches data from a MySQL database table named "customer" and displays it in a tkinter table widget.
                        conn=mysql.connector.connect(host="localhost",user="root",password="Bansal@2021",database="hms")
                        my_cursor=conn.cursor()
                        my_cursor.execute("select * from customer")
                        rows=my_cursor.fetchall()
                        if len(rows)!=0:
                                self.Cust_details_Table.delete(*self.Cust_details_Table.get_children())
                                for i in rows:
                                        self.Cust_details_Table.insert("", END,values=i)
                                conn.commit()
                        conn.close()

# ===============GET CURSOR==============

    def get_cuersor(self,event):
        cusrsor_row=self.Cust_details_Table.focus()
        content=self.Cust_details_Table.item(cusrsor_row)  #cusrsor_row is a variable
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

# =====================UPDATE DATA===================

    def update(self):
        if self.var_mobile.get()=="":
                messagebox.showerror("Error","Please enter the mobile number",parent=self.root)
        else:
                conn=mysql.connector.connect(host="localhost",user="root",password="Bansal@2021",database="hms")
                my_cursor=conn.cursor()
                my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                self.var_cust_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_id_proof.get(),self.var_id_number.get(),self.var_address.get(),self.var_ref.get()))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update","Customer details has been Updated sucessfully",parent=self.root)

# ============DELETE DATA=============

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mDelete>0:
                conn=mysql.connector.connect(host="localhost",user="root",password="Bansal@2021",database="hms")
                my_cursor=conn.cursor()
                query="delete from customer where Ref=%s"
                value=(self.var_ref.get(),)
                my_cursor.execute(query,value)
        else:
                if not mDelete:
                        return
        conn.commit()
        self.fetch_data()
        conn.close()                          



# =================RESET DATA=============

    def reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x=random.randint(1000, 9999)
        self.var_ref.set(str(x))

# ================SEARCHING========================


    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Bansal@2021",database="hms")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.Cust_details_Table.delete(*self.Cust_details_Table.get_children())
                for i in rows:
                        self.Cust_details_Table.insert("",END,values=i)
                conn.commit()
        conn.close()        






















if __name__ == "__main__":
        root=Tk()   #Tk means tool kit
        obj=Cust_Win(root)
        root.mainloop()