
def ajrat(list):
    dict = {}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1


    print(dict)


str = "mississippi"
ajrat(str)