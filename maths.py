from tkinter import *

root = Tk()
root.title('Simple Calculator (SC)')

firstvalue = IntVar()
secondvalue = IntVar()

firstvalue.set(1)
secondvalue.set(1)

def default():
	b1.config(relief=RAISED)
	b2.config(relief=RAISED)
	b3.config(relief=RAISED)
	b4.config(relief=RAISED)

def maker():
	firstvalue.set(1)
	secondvalue.set(1)

def forb1():
	try:
		bh = 0
		for i in range(0,999999999999999):
			root.update()
			if b1['relief']!=SUNKEN:
				break
			try:
				if bh >= 99999999999999999999999999999:
					maker()
					forb1()
				else:
					bh = (firstvalue.get())+(secondvalue.get())
					ll.config(text="Answer: "+str(bh))
			except:
				pass
	except:
		pass

def forb2():
	try:
		bh = 0
		for i in range(0,999999999999999):
			root.update()
			if b2['relief']!=SUNKEN:
				break
			try:
				if bh > 99999999999999999999999999999:
					maker()
					forb2()
				else:
					bh = (firstvalue.get())-(secondvalue.get())
					ll.config(text="Answer: "+str(bh))
			except:
				pass
	except:
		pass

def forb3():
	try:
		bh = 0
		for i in range(0,999999999999999):
			root.update()
			if b3['relief']!=SUNKEN:
				break
			try:
				if bh > 99999999999999999999999999999:
					maker()
					forb3()
				else:
					bh = (firstvalue.get())*(secondvalue.get())
					ll.config(text="Answer: "+str(bh))
			except:
				pass
	except:
		pass

def forb4():
	try:
		bh = 0
		for i in range(0,999999999999999):
			root.update()
			if b4['relief']!=SUNKEN:
				break
			try:
				if bh > 99999999999999999999999999999:
					maker()
					forb4()
				else:
					bh = (firstvalue.get())/(secondvalue.get())
					ll.config(text="Answer: "+str(bh))
			except:
				pass
	except:
		pass

def activator(value):
	if value==0:
		default()
		b1.config(relief=SUNKEN)
		forb1()
	elif value==1:
		default()
		b2.config(relief=SUNKEN)
		forb2()
	elif value==2:
		default()
		b3.config(relief=SUNKEN)
		forb3()
	elif value==3:
		default()
		b4.config(relief=SUNKEN)
		forb4()

def emp(framename,text):
	Label(framename,text=text,bg="black",fg="black").pack(side=LEFT)

f1 = Frame(borderwidth=10,bg="black")
f2 = Frame(borderwidth=10,bg="black")
f3 = Frame(borderwidth=10,bg="black")
f4 = Frame(borderwidth=10,bg="black")

b1 = Button(f1,text="Addition",bg='white',fg='black',font="system 14 bold",relief=RAISED,command=lambda:(activator(0)))
b1.pack(side=LEFT)

emp(f1,'  ')

b2 = Button(f1,text="Subtraction",bg='white',fg='black',font="system 14 bold",relief=RAISED,command=lambda:(activator(1)))
b2.pack(side=LEFT)

emp(f1,'  ')

b3 = Button(f1,text="Multiplication",bg='white',fg='black',font="system 14 bold",relief=RAISED,command=lambda:(activator(2)))
b3.pack(side=LEFT)

emp(f1,'  ')

b4 = Button(f1,text="Division",bg='white',fg='black',font="system 14 bold",relief=RAISED,command=lambda:(activator(3)))
b4.pack(side=LEFT)

Label(f2,text="            First Num:      ",font="comicsansms 14 bold",bg="black",fg="white").pack(side=LEFT)
en1 = Entry(f2,textvariable=firstvalue,font="system 14 bold",bg="white",fg="black",width=20).pack(side=LEFT)

Label(f3,text="           Second Num: ",font="comicsansms 14 bold",bg="black",fg="white").pack(side=LEFT)
en2 = Entry(f3,textvariable=secondvalue,font="system 14 bold",bg="white",fg="black").pack(side=LEFT)

f1.pack(anchor="w")
f2.pack(anchor="w")
f3.pack(anchor="w")

bh = 0

ll = Label(text="Answer: "+str(bh),font="comicsansms 14 bold",bg="black",fg="white",pady=20)
ll.pack()

root.config(bg="black")
root.mainloop()