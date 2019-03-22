


nums=[2,4,3,11,10,5,73,63]

print("------------------------------------")
#filter(function,sequence)

'''
def even(n):
	return n%2==0

evens=list(filter(even,nums))
print(evens)

'''

# but we can achieve same work using lambda
evens=list(filter(lambda n: n%2==0, nums))
odds=list(filter(lambda n: n%2!=0,nums))
print(evens,odds)

print("------------------------------------")
# map(funcion,sequence)
'''
def update(a):
	return a*2

doubles=list(map(update,evens)
print(doubles)
'''

# same thing using lambda
doubles=list(map(lambda n:n*2,evens))
print(doubles)

print("-------------------------------------")
# reduce(function,sequence)
# this reduce fn defined in module functools

'''
def summation(a,b):
	return a+b

summ=reduce(summation,doubles)
print(summ)
'''
summ=reduce(lambda a,b: a+b ,odds)
print(summ)
