n,m =map(int,raw_input().split(" "))
if(n>m):
	large=n
else:
	large=m
print max([i for i in range(1,large+1) if (n%i==0) and (m%i==0)])
