#Ascending?
#MONTH > MAX > MIN > PP(1decimal) > DAYS <= 0
#(2) > (5) > (7) > (19) > (7) below 0 


def compute_all_month_stats(filename): 
	
	try:
		file = open(filename, "r")
		file.readline() 
		file_list = [] 
		
		for line in file: 
			file_list.append(line.split(","))
		
		final_list = []
		for month in range(1,13):
			max_list = []
			min_list = []
			pp_total = [] 
			days_below = 0
			
			for x in file_list:
				if (int(x[2])) == month:
					max_list.append(float(x[5]))

			for x in file_list: 
				if (int(x[2])) == month: 
					min_list.append(float(x[7]))

			for x in file_list: 
				if (int(x[2])) == month:
					pp_total.append(float(x[19]))

			for x in file_list: 
				if (int(x[2])) == month: 
					if (float(x[7])) <= 0: 
						days_below += 1
			
			file.close()
			
			p = month
			q = max(max_list)
			r = min(min_list)
			s = "%0.1f" % sum(pp_total)
			t = days_below
			tu1 = (p,q,r,s,t)
			final_list.append(tu1) 
		return final_list
	
	except FileNotFoundError: 
		print("CSV FILE:", filename, "NOT FOUND") 

def main(): 
	filename = input("What is the name of the CSV file (include suffix!): ")
	all_stats = compute_all_month_stats(filename)

	if all_stats != None:
		for (month, max, min, precip, freezing) in all_stats:
			print(month, max, min, precip, freezing, sep=",")

			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
#!/usr/bin/env python3
#NO GLOBAL
import sys

def read_food_file(filename):
	try:
		
		food_file = open(filename, "r") 
		file_dict = {}
		for line in food_file:
			li = line.split(",")
			li[-1] = li[-1].replace("\n","")
			file_dict[li[0]] = li[1:]
	
	except FileNotFoundError: 
		print("CSV FILE:", filename, "NOT FOUND")
		return {} 

def dump_data(eat_data):
	#print("-- dump_data() not yet completed --")

	for i in sorted(eat_data):
		print(i, end=": ")
		for j in sorted(eat_data[i])[0:-1]:
			print(j, end=", ")
		print(sorted(eat_data[i])[-1])


def compute_only_eaters(life):

	eaters = []
	eaten = []
	for i in life:
		eaters.append(i)
		
		for j in life[i]:
			eaten.append(j)
			
	only_eaters = []
	
	for i in eaters:
		if i not in eaten:
			only_eaters.append(i)
	
	return sorted(only_eaters)

def compute_only_eaten(life):
	eaters = []
	eaten = []
	for i in life:
		eaters.append(i)
		
		for j in life[i]:
			eaten.append(j)
	
	only_eaten = []
	
	for i in eaten:
		if i not in eaters:
			if i not in only_eaten:
				only_eaten.append(i)
	
	return sorted(only_eaten)


def compute_fussiest_eaters(life):

	dict_eaters = {}
	
	for i in life:
		dict_eaters[i] = len(life[i])
		
	keys = []
	values = []
	
	for i in dict_eaters:
		keys.append(i)
		values.append(dict_eaters[i])
		
	fussy_eaters = []

	for i in keys:
		if min(values) == dict_eaters[i]:
			fussy_eaters.append(i)
			
	return sorted(fussy_eaters)

def compute_most_delicious(life):

	dict_eaten = {}
	
	for i in life:
		for j in life[i]:
			if j not in dict_eaten:
				dict_eaten[j] = 1
			else:
				dict_eaten[j] += 1
				
	keys = []
	values = []

	for i in dict_eaten:
		keys.append(i)
		values.append(dict_eaten[i])
		
	most_tasty = []
    
	for i in keys:
		if max(values) == dict_eaten[i]:
			most_tasty.append(i)
	
	return sorted(most_tasty)

def main(): #DONT CHANGE
	filename = input("Name of CSV file? ")
	life = read_food_file(filename)
	if life == {}:
		sys.exit(1)

	li = dump_data(life)
	print()

	li = compute_only_eaters(life)
	print("Only eaters:", ", ".join(li))
	print()

	li = compute_only_eaten(life)
	print("Only eaten:", ", ".join(li))
	print()

	li = compute_fussiest_eaters(life)
	print("Fussiest eaters:", ", ".join(li))
	print()

	li = compute_most_delicious(life)
	print("Tastiest entry:", ", ".join(li))


main()
