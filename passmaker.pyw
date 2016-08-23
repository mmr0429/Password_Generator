#!/usr/bin/python3
import time
import sys
from random import randint
try:
	from tkinter import *
except:
	print("Wrong Python Version, try 3.5")
	sys.exit(0)

def gen(il_zn):
	hl=il_zn
	x=1
	random_nums = ["0"] * hl
	password_array = ["error"] * hl
	password=""
	str_char = lambda p1,p2: str(chr(p1[p2]))
	while x < (hl+1) :
		int(random_nums[x-1])
		random_nums[x-1]=randint(33,126)
		password_array[x-1]=str_char(random_nums,x-1)
		password=password+password_array[x-1]
		x=x+1
	return password
#print ("Your password is: ",gen(12))

class User_interface(Frame):
	def pass_gen(self):
		try:
			self.how_long=int(self.field_num.get())
			self.ready_password=str(gen(self.how_long))
			self.field_pass.delete(0.0,END)
			self.field_pass.insert(0.0,self.ready_password)
		except:
			self.field_pass.delete(0.0,END)
			self.field_pass.insert(0.0,"Wrong Data Type")
	def bld(self):

		Label(self,text="How long your password should be ? ").grid(column=0,row=0,columnspan=3)

		Button(self,text="Generate",command=self.pass_gen).grid(column=1,row=2,sticky=N)

		self.field_num=Entry(self,width=4)
		self.field_num.grid(column=4,row=0,sticky=W)
		self.field_num.insert(0,"5")

		self.field_pass=Text(width=30,height=6,wrap=CHAR)
		self.field_pass.grid(row=3,column=0,columnspan=4)
		self.field_pass.insert(0.0,"-<Password>-")
	def __init__(self,sup):
		super(User_interface,self).__init__(sup)
		self.passw=""
		self.grid()
		self.bld()

window=Tk()
ui=User_interface(window)
#window.geometry("300x300")
window.mainloop()
