import os
def printtext():
    global e
    quote = e.get() 
    print(quote) 
    file= open(r"C:\Users\KIIT\Documents\Rainmeter\Skins\NewFolder\test.txt", "r+")
    lines=file.readlines()
    print("Present quote: "+lines[18][6:])
    #quote = raw_input("New quote : ")
    lines[18]="Text = "+quote
    print(lines[18])
    file.truncate(0)
    for line in lines:
        file.write(line)
    file.close()
    nf=open(r"C:\Users\KIIT\Documents\Rainmeter\Skins\NewFolder\selfQuote.ini", "r+")
    nf.truncate(0)
    for line in lines:
        nf.write(line)
    nf.close()
    os.system('cmd /c"rainmeter"')

from tkinter import *
root = Tk()
canvas1 = Canvas(root, width = 300, height = 300, bg="purple")
canvas1.pack()
root.title('Quote Changer!!!')

e = Entry(root)
e.pack()
e.focus_set()


b = Button(root,text='CHANGE',command=printtext,height=3, width=10, bg="yellow")
b.pack(side='bottom')
canvas1.create_window(150, 100, window=e)
canvas1.create_window(150, 180, window=b)
root.mainloop()
