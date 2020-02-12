def main(): 

	li1 = ['the','moo','man','went','to','school','yesterday','tomorrow']
	li2 = []
	li3 = []
	for i in li1:
		li2.append(i)
	print(li2)
	li3.append(li2)
	print(li3)

	for j in li3:
		print(len(j))

main()