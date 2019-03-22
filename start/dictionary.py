
n=int(input("team size :"))
team=[x for x in input("Enter all members of team : ").split(' ')]
m=int(input("Num of matches :"))
score={}

for i in range(1,m+1):
	print("enter value for match {} : ".format(i))
	d={}
	for k in team:
		value=int(input("score of {} : ".format(k)))
		d[k]=value
	match='match'+str(i)
	score[match]=d

print("=================================")
print(score)
print("=================================")
for match in sorted(score.keys()):
	temp=score[match]
	total=0
	for v in temp.values():
		total+=v
	
	print("total score in {} is : {} ".format(match,total))


print("==================================")
totalPlayerScore={}
for player in team:
	totalPlayerScore[player]=0

for match in score.values():
	for player in match.keys():
		totalPlayerScore[player]+=match[player]

print("total score each player")
for key,value in totalPlayerScore.items():
	print(key,value)

print("===================================")

