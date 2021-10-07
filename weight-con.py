from tkinter import *

window = Tk()
window.title("Weight Converter")
window.geometry("590x200")
window.minsize(590,200)
window.maxsize(590,200)
window.config(bg="blue")
def from_kg(): #convert kg to gram

    gram = float(value_1.get())*1000

    #convert kg to pound

    pound = float(value_1.get())*2.20462

    #convert kg to ounce

    ounce = float(value_1.get())*35.274

# Enter the converted weight to the text widget.

    t1.delete("1.0",END)
    t1.insert(END,gram)

    t2.delete("1.0",END)
    t2.insert(END,pound)

    t3.delete("1.0",END)
    t3.insert(END,ounce)

#create the label widgets

l1 = Label(window,text="Enter the weight in kg")
l1.config(bg='blue',fg='white',font=('Verdana',10,'bold'))

value_1 =StringVar()

e1 = Entry(window,textvariable=value_1)
e1.config(width=30,bg='white')

l2 = Label(window,text="Gram",bg="gray",fg="white",font="Verdana 10 bold")
l2.config(bg='blue',fg='white',font=('Verdana',10,'bold'))

l3 = Label(window,text="Pounds")
l3.config(bg='blue',fg='white',font=('Verdana',10,'bold'))

l4 = Label(window,text="Ounce")
l4.config(bg='blue',fg='white',font=('Verdana',10,'bold'))

# create the text widgets
t1 = Text(window,height=1,width=22)
t2 = Text(window,height=1,width=22)
t3 = Text(window,height=1,width=22)

#create the Button Widget
btn = Button(window,text="convert",command=from_kg)
btn.config(width=7,height=1,bg="black",fg="white",font=('verdana',7,'bold'),border="2px,solid,white")

l1.grid(row=1,column=0,padx=3,pady=3)

e1.grid(row=1,column=1,padx=3,pady=3)

btn.grid(row=1,column=2,padx=3,pady=3,ipadx=1)

l2.grid(row=2,column=0,padx=3,pady=3)
l3.grid(row=2,column=1,padx=3,pady=3)
l4.grid(row=2,column=2,padx=3,pady=3)

t1.grid(row=3,column=0,padx=3,pady=3)
t2.grid(row=3,column=1,padx=3,pady=3)
t3.grid(row=3,column=2,padx=3,pady=3)


#start the GUI
window.mainloop()
