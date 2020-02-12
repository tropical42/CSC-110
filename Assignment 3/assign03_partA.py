# d=Vi×t+12×a×t2


def dist_with_accel(x,y,z): 
	distance = x * z + (1/2) * y * (z**2)
	return distance




def main():
	vi = float(input("What is the initial velocity (m/s)? "))
	a = float(input("What is rate of acceleration (m/s^2)? "))
	t = float(input("How many seconds of travel to calculate (s)? "))

	d = dist_with_accel(vi, a, t)

	print("The distance is: ", d)


main()