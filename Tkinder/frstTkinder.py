# import tkinter
# from tkinter import messagebox
# app=tkinter.Tk()
# def data():
#     # print(v1.get())
#     # v=v1.get()
#     # l2.config(text=v)
#     # messagebox.askretrycancel("display",v1.get())
#     if vc1.get()==1:
#         print("mal selected")
#     if vc2.get()==1:
#         print("eng selected")
#     print(vr1.get())
# app.title("synnefo")
# app.minsize(400,400)
# app.maxsize(600,600)
# app.config(bg="green")
# l1=tkinter.Label(app,text="welcome",bg="green",fg="blue")
# l1.pack()
# v1=tkinter.StringVar()
# e1=tkinter.Entry(app,textvariable=v1)
# e1.pack()
# vc1=tkinter.IntVar()
# vc2=tkinter.IntVar()
# c1=tkinter.Checkbutton(app,text="mal",variable=vc1)
# c1.pack()
# c2=tkinter.Checkbutton(app,text="eng",variable=vc2)
# c2.pack()
# vr1=tkinter.IntVar()
# r1=tkinter.Radiobutton(app,text="male",value=1,variable=vr1)
# vr2=tkinter.IntVar()
# r2=tkinter.Radiobutton(app,text="female",value=2,variable=vr1)
# r1.pack()
# r2.pack()



# b1=tkinter.Button(app,text="SAVE",bg="White",fg="black",activebackground="red",activeforeground="green",padx=30,pady=30,command=data)
# b1.pack()
# l2=tkinter.Label(app)
# l2.pack()
# app.mainloop()



import tkinter
app=tkinter.Tk()
c=tkinter.Canvas(app,width=400,height=400,bg="green")
c.create_line(0,150,350,150)
c.create_rectangle(50,50,350,250,fill="red")
c.create_oval(50,50,350,250,fill="blue")
c.pack()
app.mainloop()