def main(): 

	age = int(input("What is the age of the child at the start of the RESP?: "))
	per_month = int(input("What is the amount invested per month?: "))
	a_return = int(input("What is the annual rate of return, in percent? (do not include % sign): "))

	print("age   RESP value")
	count = 17
	age_count = age
	
	while count >= age_count:
		interest = (a_return / 100) / 12
		months_saved = (18 - count) * 12
		resp_total = per_month * ((((1 + interest)**months_saved)-1)/interest)
		print(format(age + 1, "2.0f"), "    ", format(resp_total, "8.2f"))
		
		age += 1
		count -= 1
	
main()