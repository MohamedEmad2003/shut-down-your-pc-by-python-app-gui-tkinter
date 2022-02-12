from tkinter import *

def shutdown():
    import subprocess
    subprocess.call(["shutdown","-f","-s","-t",a.get()])


def restart():
    import subprocess
    subprocess.call(["shutdown","-f","-r","-t",a.get()])

root = Tk()
root.title('Shutdown Timer')
frame = Frame(master=root,width=500,height=400,bg='#37d3ff')
frame.pack()

btn1 = Button(master=frame,text='Shut down',command=shutdown).place(relx=0.14,rely=0.400,relwidth=0.700)
btn2 = Button(master=frame,text='Restart',command=restart).place(relx=0.14,rely=0.500,relwidth=0.700)
btn3 = Button(master=frame,text='Quit',command=root.destroy).place(relx=0.34,rely=0.650,relwidth=0.300)

info = Label(master=root,text=' If you want Conrtol PC do it !',font=("TKFixedFont 15 bold"),bg='#37d3ff',fg='brown').place(relx=0.20,rely=0.10,relwidth=0.600,height=30)

a = StringVar()

entry = Entry(master=frame,textvariable=a).place(relx=0.55,rely=0.300,height=25,width=120)
err = Label(master=root,text='Put Time in minutes :',font=("TKFixedFont 10 bold"),bg='#37d3ff').place(relx=0.25,rely=0.300)

root.mainloop()
