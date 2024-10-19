def toh(n,s,d,a):
	if(n==1):
		print("Move disk "+s+" to "+d+" .")
		return
	toh(n-1,s,a,d)
	print("Move disk "+s+" to "+d+" .")
	toh(n-1,a,d,s)
toh(3,'A','B','C')
