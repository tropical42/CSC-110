def main(): 

	age_of_child = int(input("What is the age of the child?: "))
	per_month = int(input("What is the amount of money invested each month?: "))
	rate_annual = int(input("What is the rate of return for the investment in % ? (do not include % sign): "))
	
	interest = (rate_annual / 100) / 12
	months_saved = (18 - age_of_child) * 12
	resp_total = per_month * ((((1 + interest)**months_saved)-1)/interest)
	
	print(format(resp_total, ".2f"))
	
main()