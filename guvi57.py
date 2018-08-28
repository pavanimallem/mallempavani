n,k=map(int,raw_input().split())
list=[int(x) for x in raw_input().split()]
count=0
for i in list:
	if(i==k):
	  count=count+1
print(count)
