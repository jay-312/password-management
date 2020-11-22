def login():
    import tkinter as tk
    import sql
    import list
    import search
    import add
    import delete
    
    #==funtions==
    
    def Add():
        add.add(B)
    
    def Search():
        search.search(B)
        pass
    
    def List():
        list.list(B)
        
    def Delete():
        delete.delete(B)   
        
    #== Main ==
        
    root=tk.Toplevel()
    root.title('Password Manager')
    root.iconbitmap('icon.ico')
    root.geometry('450x200')
    
    f=tk.Frame(root,bg='Lavender',bd=2,relief=tk.RAISED, pady=10,padx=10)
    f.place(relx=0.5,rely=0.5,anchor='c')
    
    for i in sql.cur.fetchall() :
        A=i[0]
        B=i[1]
        
    tk.Label(f, text="Hello "+A,bg='Lavender', font='Helvetica 18 bold', pady=10,padx=10).grid(row=0, column=0, columnspan=4 )
        
    add_image = tk.PhotoImage(file='Add.gif')
    tk.Button(f,image=add_image,command=Add).grid(row=1,column=0,pady=10,padx=20)
    
    search_image = tk.PhotoImage(file='Search.gif')
    tk.Button(f,image=search_image,command=Search).grid(row=1,column=1,pady=10,padx=10)
    
    list_image = tk.PhotoImage(file='List.gif')
    tk.Button(f,image=list_image,command=List).grid(row=1,column=2,pady=10,padx=10)

    delete_image = tk.PhotoImage(file='delete.gif')
    tk.Button(f,image=delete_image,command=Delete).grid(row=1,column=3,pady=10,padx=20)
        
    root.mainloop()
