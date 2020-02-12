def main(): 

	for i in range(10, 0, -1):
		for j in range(i):
			if j < (i-1): 
				print(j, end=",")
			else:
				print(j)

main()