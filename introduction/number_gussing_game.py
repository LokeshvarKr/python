import random

r1,r2=input("Enter range comma seperated r1,r2 : ").split(",")
r1=int(r1)
r2=int(r2)

while True:
	n=random.randrange(r1,r2)
	num=int(input("Guess a number from r1 - r2 : "))
	if n == num:
		print("congratulation! you won the game.")
		break;
	else:
		if num <= n-10:
			print("your guess was too low")
		elif num >= n+10 :
			print("your guess was too low")
		else:
			print("your guess was too near")


	print("it was "+str(n))


