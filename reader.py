#文本文件的打开,保存和另存；可一键访问历史记录（五个最近的历史记录（不重复））。
import tkinter as tk
#文件选择对话框
import os,json
import tkinter.filedialog
from tkinter import messagebox
#主窗口
root  =tk.Tk()
root.title("Text reader made by yy")
root.geometry('500x500')
##输入窗口（仅仅用作显示）
res = tk.Variable()
entry = tk.Entry(root,textvariable = res,width = 40)
res.set('Selected files:')
entry.pack()
 
def add_path(path1):
	global path_list
	try:
		with open('C:\yy.txt','r') as f:
			path_list = json.load(f)
			if path1 not in path_list:
				while len(path_list) > 4:
					path_list = path_list[1:]
				else:
					path_list.append(path1)
			else:
				pass
		with open('C:\yy.txt', 'w') as f:
			json.dump(path_list, f)
	except:
		with open('C:\yy.txt','w') as f:
			path_list = []
			path_list.append(path1)
			json.dump(path_list,f)
 
#初始化列表长度
try:
	with open('C:\yy.txt', 'r') as f:
		path_list = json.load(f)
		if len(path_list) < 5:
			while True:
				path_list.append('C:')
				if len(path_list) >= 5:
					break
except:
	path_list = []
 
 
def func1():		#open
	global filename,res
	filename = tkinter.filedialog.askopenfilename(filetypes = [(" please open txt file", "*.txt")])
	add_path(filename)
	try:
		with open(filename,'r') as f:
		 content = f.read()
		text.delete(0.0,tk.END)
		text.insert(tk.INSERT,content)
		basename = os.path.basename(filename)
		res.set('%s'%basename)
		button4.config(text = os.path.basename(path_list[-1]))
		button5.config(text = os.path.basename(path_list[-2]))
		button6.config(text = os.path.basename(path_list[-3]))
		button7.config(text = os.path.basename(path_list[-4]))
		button8.config(text = os.path.basename(path_list[-5]))
 
	except:
		pass
 
def func2():		#save
	with open(filename,'w') as f:
		try:
			f.write(text.get(0.0,tk.END))
			f.flush()
			basename = os.path.basename(filename)
			save_succed = messagebox.showinfo(title='message', message='%s  save succed' % basename)
			print(save_succed)
		except:
			save_error = messagebox.showinfo(title = 'unfortunately ',message = 'save failure')
			print(save_error)
 
#打开历史记录对应的文件
def func3(button,filename):		#open
	global res,button4
	add_path(filename)
	try:
		with open(filename,'r') as f:
		 content = f.read()
		text.delete(0.0,tk.END)
		text.insert(tk.INSERT,content)
		basename = os.path.basename(filename)
		res.set('%s'%basename)
	except:
		pass
 
def save_as():
	filename1 = tkinter.filedialog.asksaveasfilename()
	add_path(filename1)
	with open(filename1, 'w') as f:
		f.write(text.get(0.0, tk.END))
		basename = os.path.basename(filename1)
		save_succed = messagebox.showinfo(title='message', message='%s  saveas  succed' % basename)
		print(save_succed)
#制作底部框体和（打开保存另存）按钮
fm2 = tk.Frame(root)
button1 = tk.Button(fm2,text = 'open',command = func1)
button1.pack(side = "left")
 
button2 = tk.Button(fm2,text = 'save',command = func2)
button2.pack(side = "left")
 
button3 = tk.Button(fm2,text = 'saveas',command = save_as)
button3.pack(side = "left")
 
fm2.pack(side = 'bottom')
 
#制作右侧的历史记录按钮按钮
 
 
#右侧总框架
fm3 = tk.Frame(root)
#右侧label
label_right = tk.Label(fm3,text  = '历史记录 :')
label_right.pack(side = 'top')
#历史文件访问地址获取，通过path_list
a,b,c,d,e = os.path.basename(path_list[-1]),os.path.basename(path_list[-2]),os.path.basename(path_list[-3]),os.path.basename(path_list[-4]),os.path.basename(path_list[-5])
#右侧历史记录的键
#注意lambda花式传参方式
button4 = tk.Button(fm3,text = a,command = lambda func1 = func3:func3(button4,path_list[-1]))
button4.pack(side = "top")
 
button5 = tk.Button(fm3,text = b,command = lambda func1 = func3:func3(button5,path_list[-2]))
button5.pack(side = "top")
 
button6 = tk.Button(fm3,text = c,command = lambda func1 = func3:func3(button6,path_list[-3]))
button6.pack(side = "top")
 
button7 = tk.Button(fm3,text = d,command = lambda func1 = func3:func3(button6,path_list[-4]))
button7.pack(side = "top")
 
button8 = tk.Button(fm3,text = e,command = lambda func1 = func3:func3(button6,path_list[-5]))
button8.pack(side = "top")
 
fm3.pack(side = 'right')
 
 
 
#滚动条
scroll = tk.Scrollbar()
scroll.pack(side = tk.RIGHT,fill = tk.Y)
#文本
text = tk.Text(root,width = 200,height = 20)
text.pack(side = tk.LEFT,fill = tk.Y)
#滚动条和文本相互绑定
scroll.config(command = text.yview)
text.config(yscrollcommand = scroll.set)
 
root.mainloop()
