
def ajrat(list = []):
    dict = {}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1


    print(dict)


myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
ajrat(myList)