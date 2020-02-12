def print_mult_table(start, end):
	if start > end:
		print("Error; Starting value is larger than end value.")
	elif start < 0: 
		print("Error; Starting value is negative.")
	elif (end - start) > 14:
		print("Error; Difference between start value and end value is greater than 14.")
	
	else:
		print(format("",'5s'),'|', end="")
	for i in range(start,end):
		print(format(i, '6d'),'|', end="")
	print(format(end, '6d'))
	print()
	
	for j in range(start,end+1): 
		print(format(j,'4d'), ' | ', end="")
		for k in range(start,end): 
			print (format((j * k),'5d'), ": ", end="")
		print(format(j*end, '5d'),end="\n")

		
def main():
	start = int(input("Start of table "))
	end = int(input("End of table "))
	print_mult_table(start, end)

main()
