# Problem 2

def expand(rng):

    #this function takes in a list of parameters in the form of a comma separated string
    #it returns a new int based list with all of the numerical values presented
    #it converts ranges into its respective numbers that left inclusive and right non-inclusive

    
    ran =[]

    for i in rng.split(sep=','):
        if '-' not in i:
            if int(i) not in ran:
                ran.append(int(i))
        else:
            n = i.split(sep="-")
            n_int = list(map(int, n))
            b = int(n[0])
            while b != n_int[-1]:
                if int(b) not in ran:
                    ran.append(b)
                    b += 1
    
    #sort the final list
    ran.sort()

    return(ran)


print(expand("1,2-5,5,6-10"))
print(expand("6-10,1,2-5,5"))