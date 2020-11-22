def delete(n):
    import tkinter as tk
    import sql
    
    #--functions--
    def Delete():
        sql.Delete(n, site.get(), ID.get())
        m.config(text='Data successfully deleted')   
                
    #--main--
    root=tk.Toplevel()
    root.title('Delete')
    root.iconbitmap('icon.ico')
    root.geometry('250x200')
    
    site = tk.StringVar()
    ID = tk.StringVar()
    
    f=tk.Frame(root,bg='Lavender',bd=2,relief=tk.RAISED, pady=10,padx=10)
    f.place(relx=0.5, rely=0.5, anchor='c')
    
    tk.Label(f,text='Site : ',bg='Lavender').grid(row=0,column=0,sticky='e')
    tk.Entry(f, textvariable=site).grid(row=0,column=1)

    tk.Label(f,text='User ID : ',bg='Lavender').grid(row=1,column=0,sticky='e')
    tk.Entry(f, textvariable=ID).grid(row=1,column=1)

    m=tk.Label(f,text='',bg='Lavender',fg='red')
    m.grid(row=3,column=0,columnspan=2)
    
    tk.Button(f,text='Delete',bg='Lavender', width=10, command=Delete).grid(row=4, column=0, columnspan=2,pady=10)    
    
    root.mainloop()