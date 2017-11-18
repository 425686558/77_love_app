#!/usr/bin/python3
#encoding=utf8
import tkinter
from tkinter import *
class window:
	__width = 0
	__height = 0
	window = tkinter.Tk()
	__arg = {
	"int":lambda self,tp:self.window.winfo_screenwidth() if tp == 0 else tp,
	"float":lambda self,tp:self.window.winfo_screenwidth() if self == 0 else int(math.ceil(tp * self.__window.winfo_screenwidth()))}
	
	def __init__(self,width = 0,height = 0):
		self.__width = self.__arg[type(width).__name__](self,width)
#		if (type (width) == int):
#			if (0 == width):
#				self.__width = self.__window.winfo_screenwidth()
#			else:
#				self.__width = width
#		else:
#			raise Exception("width should be integer")

		if (type (height) == int):
			if (0 == height):
				self.__height = self.window.winfo_screenheight()
			else:
				self.__height = height
		else:
			raise Exception("height should be integer")

	def size(self):
		print("width:%d height:%d" %(self.__width,self.__height))

a = window()
a.size()
#top = tkinter.Tk()
#top.title("吃饭啦")
#Frame(height = 600,width = 800).pack()  
#top.mainloop()
