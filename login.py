from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
import mysql.connector

def main():
        win=Tk()
        app=Login_Window(win)
        win.mainloop()





class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        self.bg=ImageTk.PhotoImage(file="E:\hms\hotel\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)


        img1=Image.open(r"E:\hms\hotel\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,borderwidth=0,bg="black")
        lblimg1.place(x=730,y=175,width=100,height=100)

# get started 

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

#label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)


        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)


        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)


        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)


        # ==============ICON Image===============
        img2=Image.open(r"E:\hms\hotel\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimg2,borderwidth=0,bg="black")
        lblimg1.place(x=650,y=323,width=25,height=25)       


        # ==============ICON Image===============
        img3=Image.open(r"E:\hms\hotel\lock-512.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimg2,borderwidth=0,bg="black")
        lblimg1.place(x=650,y=395,width=25,height=25)    


        #=============== loginButton===============

        loginbtn=Button(frame, text="Login",command=self.login,font=("times new roman",20,"bold"),bd=3,relief=RAISED,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)


        #=================RegistrButton===============
        
        registerbtn=Button(frame, text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #===================forgetpasswordButton============

        btn_login=Button(frame, text="Forget Password",command=self.forget_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        btn_login.place(x=10,y=370,width=160)



    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="s@hm" and self.txtpass.get()=="123":
            
            obj=HotelManagementSystem(self)
            
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Bansal@2021",database="hms")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(self.var_email.get(),self.var_pass.get()))

            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Acess Only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=hms(self.new_window)  #=====================Hotel management system
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()            


    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Bansal@2021",database="hms")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")




# ====================================REGISTER FORM================================


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")



# ==================Variable=======================


        self.var_fname=StringVar()
        self.var_lname=StringVar()        
        self.var_contact=StringVar()        
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()





#======================Background Image=================
        self.bg=ImageTk.PhotoImage(file=r"E:\hms\hotel\nature.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

# =====================Left Image=================

        self.bg1=ImageTk.PhotoImage(file=r"E:\hms\hotel\LoveSove.jpg")
        bg_lbl=Label(self.root,image=self.bg1)
        bg_lbl.place(x=50,y=100,width=470,height=550)

# ===============MAIN FRAME======
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)


        register_lbl=Label(frame, text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)        


# ====================Label AND ENTERY================


#=========row1

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)


# ============row2

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

# =============row3

        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.como_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.como_security_Q["values"]=("Select","Your Birth Place","Your Favorite Place","Your Pet Name")
        self.como_security_Q.place(x=50,y=270,width=250)          
        self.como_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)


# ============row4

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)



# ==============CHECK Button====================
        self.var_check=IntVar()
        self.var_checkbtn=Checkbutton(frame,text="I agree the Terms & conditions",variable=self.var_check,font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.var_checkbtn.place(x=50,y=380)


# =================Button============
        img=Image.open(r"E:\hms\hotel\register-now-button1.jpg")
        img=img.resize((200,55),Image.ANTIALIAS)     #ANTILIASED HIGH TO CONVERT LOW AND LOW TO HIGH IMAGE
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,font=("times new roman",15,"bold"),borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)


        img1=Image.open(r"E:\hms\hotel\loginpng.png")
        img1=img1.resize((200,45),Image.ANTIALIAS)    
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,font=("times new roman",15,"bold"),borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)



    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All field are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Bansal@2021",database="hms")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(self.var_fname.get(),self.var_lname.get(),
                self.var_contact.get(),self.var_email.get(),self.var_securityQ.get(),self.var_securityA.get(),self.var_pass.get()))

            conn.commit()
            conn.close()
            messagebox.showinfo("success","Register Sucessfully")







if __name__=="__main__":
    main()