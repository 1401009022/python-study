import tkinter

top = tkinter.Tk()

hello = tkinter.Label(top, text="hello world!")
hello.pack()

quit = tkinter.Button(top, text="QUIT",bg="red",fg="white",comman=top.quit)
quit.pack(fill=tkinter.X, expand=1)

tkinter.mainloop()