STANLEY_CUP_WINNERS = [(2018, 'Washington Capitals'), (2017, 'Pittsburgh Penguins'), (2016, 'Pittsburgh Penguins'), 
               (2015, 'Chicago Blackhawks'), (2014, 'Los Angeles Kings'), (2013, 'Chicago Blackhawks'), 
               (2012, 'Los Angeles Kings'), (2011, 'Boston Bruins'), (2010, 'Chicago Blackhawks'), 
               (2009, 'Pittsburgh Penguins'), (2008, 'Detroit Red Wings'), (2007, 'Anaheim Ducks'), 
               (2006, 'Carolina Hurricanes'), (2004, 'Tampa Bay Lightning'), (2003, 'New Jersey Devils'), 
               (2002, 'Detroit Red Wings'), (2001, 'Colorado Avalanche'), (2000, 'New Jersey Devils'), 
               (1999, 'Dallas Stars'), (1998, 'Detroit Red Wings'), (1997, 'Detroit Red Wings'), 
               (1996, 'Colorado Avalanche'), (1995, 'New Jersey Devils'), (1994, 'New York Rangers'), 
               (1993, 'Montreal Canadiens'), (1992, 'Pittsburgh Penguins'), (1991, 'Pittsburgh Penguins'), 
               (1990, 'Edmonton Oilers'), (1989, 'Calgary Flames'), (1988, 'Edmonton Oilers'), 
               (1987, 'Edmonton Oilers'), (1986, 'Montreal Canadiens'), (1985, 'Edmonton Oilers'), 
               (1984, 'Edmonton Oilers'), (1983, 'New York Islanders'), (1982, 'New York Islanders'), 
               (1981, 'New York Islanders'), (1980, 'New York Islanders'), (1979, 'Montreal Canadiens'), 
               (1978, 'Montreal Canadiens'), (1977, 'Montreal Canadiens'), (1976, 'Montreal Canadiens'), 
               (1975, 'Philadelphia Flyers'), (1974, 'Philadelphia Flyers'), (1973, 'Montreal Canadiens'), 
               (1972, 'Boston Bruins'), (1971, 'Montreal Canadiens'), (1970, 'Boston Bruins'), 
               (1969, 'Montreal Canadiens'), (1968, 'Montreal Canadiens'), (1967, 'Toronto Maple Leafs'), 
               (1966, 'Montreal Canadiens'), (1965, 'Montreal Canadiens'), (1964, 'Toronto Maple Leafs'), 
               (1963, 'Toronto Maple Leafs'), (1962, 'Toronto Maple Leafs'), (1961, 'Chicago Blackhawks'), 
               (1960, 'Montreal Canadiens'), (1959, 'Montreal Canadiens'), (1958, 'Montreal Canadiens'), 
               (1957, 'Montreal Canadiens'), (1956, 'Montreal Canadiens'), (1955, 'Detroit Red Wings'), 
               (1954, 'Detroit Red Wings'), (1953, 'Montreal Canadiens'), (1952, 'Detroit Red Wings'), 
               (1951, 'Toronto Maple Leafs'), (1950, 'Detroit Red Wings'), (1949, 'Toronto Maple Leafs'), 
               (1948, 'Toronto Maple Leafs'), (1947, 'Toronto Maple Leafs'), (1946, 'Montreal Canadiens'), 
               (1945, 'Toronto Maple Leafs'), (1944, 'Montreal Canadiens'), (1943, 'Detroit Red Wings'), 
               (1942, 'Toronto Maple Leafs'), (1941, 'Boston Bruins'), (1940, 'New York Rangers'), 
               (1939, 'Boston Bruins'), (1938, 'Chicago Blackhawks'), (1937, 'Detroit Red Wings'), 
               (1936, 'Detroit Red Wings'), (1935, 'Montreal Maroons'), (1934, 'Chicago Blackhawks'), 
               (1933, 'New York Rangers'), (1932, 'Toronto Maple Leafs'), (1931, 'Montreal Canadiens'), 
               (1930, 'Montreal Canadiens'), (1929, 'Boston Bruins'), (1928, 'New York Rangers'), 
               (1927, 'Ottawa Senators')]



def winning_years(query_team): 
	STANLEY_CUP_WINNERS.sort()
	li1 = []
	
	for j in STANLEY_CUP_WINNERS:
		for i in j: 
			if query_team == i: 
				li1.append(j[0])
	return li1

	
def main():
	team_name = (input("What team are you searching for? "))
	winning_years(team_name)
	
	temp = winning_years(team_name)
	if len(temp) == 0: 
		print("Has not yet won the Stanley Cup")
	else:
		for x in temp: 
			print(x)
main()