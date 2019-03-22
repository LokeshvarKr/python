a=10
b=7
# 1
print("--------------------------------------")
def something():
	a=15
	print("in function ",a)

something()
print('outside',a)

# 2
print("\n--------------------------------------")
def see():
	print("in function ",a)

see()
print('outside',a)

# 3
print("\n--------------------------------------")
def see_glob_concpt():
	global a
	a=15;


see_glob_concpt()
print('outside',a)

# 4
print("\n--------------------------------------")
def global_local():
	a=100
	x=globals()['a']
	print("in fun local a ",id(a),a)
	print("in fun global a ",id(x),x)

global_local()
print('outside',id(a),a)

# 5
print("\n--------------------------------------")
def glob_con():
	x=globals()['b']
	print('in fun x as global b',id(x),x)

	# changing value of global b but it fails to do so 
	x=111
	print('in fun (id of x != id of global b ))',id(x),x)

	# to change value in global b do
	globals()['b']=8
	# see the value of b now outside


print('outside b',id(b),b)
glob_con()
print('outside b ',id(b),b)
