# Problem 1

def isect(s1, s2):

    #this is a function that finds similar numbers from two string input parameters
    #the parameters mirror a list but are actually strings with values separated by commas
    #the final returned value is a new list that removes duplicates, sorts, only counts numbers with a 2, and the values are ints

    list1 = s1.split(sep=",")
    list2 = s2.split(sep=",")

    list1_clean = []
    list2_clean = []

    list1_cleaner = []
    list2_cleaner = []

    matches = []

    #remove duplicates
    for i in list1:
        if i not in list1_clean:
            list1_clean.append(i)
    for i in list2:
        if i not in list2_clean:
            list2_clean.append(i)

    #only twos
    for i in list1_clean:
        if "2" in i:
            list1_cleaner.append(i)
    for i in list2_clean:
        if "2" in i:
            list2_cleaner.append(i)

    #matches
    for i in list1_cleaner:
        if i in list2_cleaner:
            matches.append(i)
    
    #make int and sort
    match = list(map(int, matches))
    match.sort()

    
    return(match)

print(isect("3,123,201,10,12,20", "20,3,201,124,0,12"))
print(isect("20,12,20,201", "201,20,20,12"))