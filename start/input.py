
# run first commented code

'''
ch1 = input("Enter a char ")[0]
ch2 = input("Enter a char ")
print(ch1,type(ch1))
print(ch2,type(ch2))

exp = input("Enter a char ")
print(eval(exp))

'''

# for fetching arguments which is given by user while 
#running this code using command line we have to import 
#sys module an then we access like this

import sys
file_name=sys.argv[0]
x=int(sys.argv[1])
y=int(sys.argv[2])
print(file_name)
print(x+y)