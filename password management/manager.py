import re
import tkinter as tk
import sql
import login

# --- functions ---

def sign_in():
    if(sql.CheckUser(
      signin_user.get(),
      signin_password.get()) is False):
        
        m2.config(text='Incorrect User name or Password.')
    else:
        login.login()
        

def sign_up():
    # []    A set of characters    "[a-m]"    
    # \    Signals a special sequence (can also be used to escape special characters)    "\d"    
    # .    Any character (except newline character)    "he..o"    
    # ^    Starts with    "^hello"    
    # $    Ends with    "world$"    
    # *    Zero or more occurrences    "aix*"    
    # +    One or more occurrences    "aix+"    
    # {}    Exactly the specified number of occurrences    "al{2}"    
    # |    Either or    "falls|stays"    
    # ()    Capture and group
    regpass = "^[A-Z][\w(!@#$%^&*_+?)+]{8,}$"
    reguser ='\w+'
    if(reg_name.get() ==""):        # Check if name is empty
        m.configure(text='Name is mandatory for registration.')
        
    elif(reg_user.get() ==""):      # Check if User name is empty
        m.configure(text='User Name is mandatory for registration.')
    
    elif not ( re.search(reguser,reg_user.get() ) ):   
        m.configure(text='Special character allowed is \'_\'')
    
    elif( sql.UserAvailability(reg_user.get()) is False ):      # Check if user_name already exists
        m.configure(text='Account already exists.')
            
    elif not ( re.search(regpass,reg_password.get() ) ):   
         m.configure(text='''-> Spaces and empty sets are not allowed.
        \n -> First character should be a capital letter.
        \n -> Password must be greater than 8 character. ''')
         
    elif (reg_password.get() != reg_cnfpassword.get()):     # Check if password and confirm doesn't match
        m.configure(text='-> Password and Confirm Password must match.')
        
    else :
        sql.Register(reg_name.get(),
                    reg_user.get(),
                    reg_password.get() )
        m.configure(text='You have successfully registered')



# --- main ---

root = tk.Tk()
root.title('Password Manager')
root.iconbitmap('icon.ico')
root.geometry('500x500')

signin_user = tk.StringVar()
signin_password = tk.StringVar()
reg_name = tk.StringVar()
reg_user = tk.StringVar()
reg_password = tk.StringVar()
reg_cnfpassword = tk.StringVar()


f = tk.Frame(root,bg='Lavender',bd=2,relief=tk.RAISED, pady=10,padx=10)
f.place(relx=0.5, rely=0.5, anchor='c')

tk.Label(f, text="Sign In",bg='Lavender', font='Helvetica 18 bold').grid(row=0, column=0, columnspan=2)

tk.Label(f, text='User Name : ',bg='Lavender').grid(row=1, column=0, sticky='e')
tk.Entry(f, textvariable=signin_user).grid(row=1, column=1)

tk.Label(f, text='Password : ',bg='Lavender').grid(row=2, column=0, sticky='e')
tk.Entry(f, textvariable=signin_password,show='*').grid(row=2, column=1)

m2 = tk.Label(f, text='',bg='Lavender', fg="red")
m2.grid(row=3, column=0, columnspan=2, sticky='we')

tk.Button(f, text="Sign In",bg='Lavender', width=10, command=sign_in).grid(row=4, column=0, columnspan=2)

tk.Label(f, text="Sign up",bg='Lavender', font='Helvetica 18 bold').grid(row=5, column=0, columnspan=2, pady=20)

tk.Label(f, text="Name : ",bg='Lavender').grid(row=6, column=0, sticky='e')
tk.Entry(f, textvariable=reg_name).grid(row=6, column=1)

tk.Label(f, text="User Name : ",bg='Lavender').grid(row=7, column=0, sticky='e')
tk.Entry(f, textvariable=reg_user).grid(row=7, column=1)

tk.Label(f, text="Password : ",bg='Lavender').grid(row=8, column=0, sticky='e')
tk.Entry(f, textvariable=reg_password,show='*').grid(row=8, column=1)

tk.Label(f, text="Confirm password : ",bg='Lavender').grid(row=9, column=0, sticky='e')
tk.Entry(f, textvariable=reg_cnfpassword ,show='*').grid(row=9, column=1)

m = tk.Label(f, text='',bg='Lavender', fg="red")
m.grid(row=10, column=0, columnspan=2, sticky='we')

tk.Button(f, text="Sign Up",bg='Lavender', width=10, command=sign_up).grid(row=11, column=0, columnspan=2)

root.mainloop()
