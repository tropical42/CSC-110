MIDYEAR_POPULATION = [(1971, 21962032), (1972, 22218463), (1973, 22491777), (1974, 22807969), (1975, 23143275), 
                      (1976, 23449808), (1977, 23725843), (1978, 23963203), (1979, 24201544), (1980, 24515667),
                      (1981, 24819915), (1982, 25116942), (1983, 25366451), (1984, 25607053), (1985, 25842116),
                      (1986, 26100278), (1987, 26446601), (1988, 26791747), (1989, 27276781), (1990, 27691138),
                      (1991, 28037420), (1992, 28371264), (1993, 28684764), (1994, 29000663), (1995, 29302311),
                      (1996, 29610218), (1997, 29905948), (1998, 30155173), (1999, 30401286), (2000, 30685730),
                      (2001, 31020596), (2002, 31358418), (2003, 31641630), (2004, 31938004), (2005, 32242364),
                      (2006, 32570505), (2007, 32887928), (2008, 33245773), (2009, 33628571), (2010, 34005274), 
                      (2011, 34342780), (2012, 34750545), (2013, 35152370), (2014, 35535348), (2015, 35832513), 
                      (2016, 36264604), (2017, 36708083)]
test_list = [(1900, 10000), (1901, 10100), (1902, 10211), (1903, 10287)]
def greatest_increase(pop_stats):

    li1 = [] #YEAR LIST
    li2 = [] #POPULATION LIST
    li3 = [] #POPULATION-INCREASE LIST 

    a = 0
    b = 1
    for (x,y) in pop_stats:
        li1.append(x)
        li2.append(y)

    for i,j in zip(li2[0:],li2[1:]):
        li3.append(li2[b]-li2[a])
        a += 1
        b += 1

    value1 = li1[li3.index(max(li3))+1]
    max_value = max(li3)

    return value1, max_value

def smallest_increase(pop_stats):

    li1 = [] #POPULATION LIST 
    li2 = [] #YEAR LIST
    li3 = [] #POPULATION-INCREASE LIST

    for (x,y) in pop_stats:
        li2.append(x)
        li1.append(y)

    q = 0 
    p = 1 
    for i,j in zip(li1[0:],li1[1:]):
        li3.append(li1[p]-li1[q])
        q += 1
        p += 1

    value1 = li2[li3.index(min(li3))+1]
    min_value = min(li3)

    return value1,min_value

def average_percentage_increase(pop_stats):

    li1 = [] #YEAR LIST
    li2 = [] #POPULATION LIST
    li3 = [] #AVERAGE INCREASE LIST

    for (x,y) in pop_stats:
        li1.append(x)
        li2.append(y)

    a = 0
    b = 1

    for i,j in zip(li2[0:],li2[1:]):
        li3.append((li2[b]/li2[a])-1)
        a += 1
        b += 1

    avg_inc = 100*(sum(li3) / len(li3))

    return avg_inc

def main():
    year, increase = greatest_increase(MIDYEAR_POPULATION)
    print("Greatest increase: ", year, increase)
    
    year, increase = smallest_increase(MIDYEAR_POPULATION)
    print("Smallest increase: ", year, increase)
    
    average = average_percentage_increase(MIDYEAR_POPULATION)
    print("Average percentage increase: ", format(average, ".2f"), "%", sep="")

main()