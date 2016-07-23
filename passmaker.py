import time
from random import randint
print ("Password generator v1\nHow long Your password should be ?")
hl=int(input(":"))
x=1
random_nums = ["0"] * hl
password_array = ["error"] * hl
password=""
str_char = lambda p1,p2: str(chr(p1[p2]))
while x < (hl+1) :
	int(random_nums[x-1])
	random_nums[x-1]=randint(33,126)
	password_array[x-1]=str_char(random_nums,x-1)
#	print ("DEBUG: ",random_nums[x-1]," ",password_array[x-1])
	password=password+password_array[x-1]
	x=x+1
#animation thing
"""
for z in range (1,11):
#	time.sleep(0.2)
	print("%",end="")
"""	
print ("Your password is: ",password)
