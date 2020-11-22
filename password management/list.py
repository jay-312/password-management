def list(n):
    import tkinter as tk
    from tkinter import ttk
    import sql
    
    root=tk.Toplevel()
    root.title('List')
    root.iconbitmap('icon.ico')
    root.geometry('450x300')
    
    f=tk.Frame(root,bg='Lavender',bd=2,relief=tk.RAISED, pady=10,padx=10)
    f.place(relx=0.5, rely=0.5, anchor='c')
    
    tree=ttk.Treeview(f, columns=('Sr no','site', ' User Name   Password'), selectmode="extended")
    tree.heading('#0', text='Sr No.', anchor=tk.CENTER)
    tree.heading('#1', text='Site', anchor=tk.CENTER)
    tree.heading('#2', text='User Name', anchor=tk.CENTER)
    tree.heading('#3', text='Password', anchor=tk.CENTER)
    tree.column('#0', stretch=tk.YES, minwidth=50, width=100)
    tree.column('#1', stretch=tk.YES, minwidth=50, width=100)
    tree.column('#2', stretch=tk.YES, minwidth=50, width=100)
    tree.column('#3', stretch=tk.YES, minwidth=50, width=100)
    tree.grid(row=2, column=3, columnspan=4, sticky='news')
    
    sql.cur.execute('select * from '+n)
    x=sql.cur.fetchall()
    count=1
    for i in x:
        tree.insert('','end',text=count,values=(i[0],i[1],i[2]))
        count +=1
    
    root.mainloop()