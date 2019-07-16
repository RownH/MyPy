import os
import time
import random
def main():
	content='beijing welcome to you'
	while True:
		os.system('cls')
		print(content)
		time.sleep(2)
		content=content[1:]+content[0]
def test1(code_len=4):
	rangex='123456789abcdefghijk';
	code=''
	for x in range(0,code_len):
		index=random.randint(0,len(rangex)-1)
		code+=rangex[index]
	print(code)

def get_suffix(filename,has_dot=False):
  
    pos=filename.rfind('.')
    if 0<pos<len(filename)-1:
        index=pos if has_dot else pos+1
        return filename[index:]
    else:
        return ''

def print_board(board):
    print()
