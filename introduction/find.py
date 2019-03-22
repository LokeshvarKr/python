name="harsha is a good girl she is so beautifull and so kind"
# replace method 
#replace all 'so' by 'too'
print(name.replace("so","too"))

#replace 1st one 'so' by 'too'
print(name.replace("so","too",1))

#replace first two 'so' by 'too'
print(name.replace("so","too",2))

#replace first five 'so' by 'too'
print(name.replace("so","too",5))


# find method returns position (integer value)
print(name.find("is"))
print(name.find("is",0))
print(name.find("is",1))
print(name.find("is",5))

print(name.find("z",5))

# find position of second is 
position1=name.find("is")
positon2=name.find("is",position1+1)
print(positon2)
