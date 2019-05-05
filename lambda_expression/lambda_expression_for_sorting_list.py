authors=['Ankit K kain','jaggu Aaj','Karumanchi','Kanak Kata',"Rahul Kumar Vishwkarma","Raja k Thakur"]


# sort the above author list by last name

print(authors)
print()

#case sensitive sorting
# authors.sort(key=lambda name: name.split()[-1])

#case insensitive sorting
authors.sort(key=lambda name: name.split()[-1].lower())


print(authors)
