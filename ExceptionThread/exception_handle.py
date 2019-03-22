print("=======================================")

a=5
b=6

try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("resource close")
    print(e)

print("=======================================")

a=5
b=0

try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("resource close")
    print(e)


print("some work ")
print("resource close")

print("=======================================")

try:
    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print("Value Error")
except Exception as e:
    print("Something wrong....... Exception is " , e)
finally :
    print("resource close")

print("byeeee......")