#!/usr/bin/python3
#encoding=utf8
from tkinter import *
import math
class LWindow(Tk):
	__screen_width = 0
	__screen_height = 0
	__width = 0
	__height = 0
	__title = ""
	__arg = {"int":lambda sc,arg:sc if arg == 0 else arg,
		 "float":lambda sc,arg:sc if arg == 0 else int(math.ceil(arg * sc))}
	__arg_process = lambda self,sc,arg:self.__arg[type(arg).__name__](sc,arg)
	
	def __init__(self, width = 0, height = 0,title = ""):
		super(LWindow, self).__init__()
		self.__screen_width = self.winfo_screenwidth()
		self.__screen_height = self.winfo_screenheight()
		self.__width = self.__arg_process(self.__screen_width, width)
		self.__height = self.__arg_process(self.__screen_height, height)
		self.__title = title
		self.title(self.__title)
		self.geometry("%dx%d+%d+%d" % (self.__width, self.__height, 0, 0))
		self.mainloop()

	def size(self):
		print("width:%d height:%d" %(self.__screen_width,self.__screen_height))

a = LWindow(0.5,0.5,"hello")
