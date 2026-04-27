list = [1, 2, 3, 4, 5]
list2 = [11, 22, 33, 44, 55]

def newlist(list,list2):
    newlist= []
    counter = 0
    while len(newlist) != (len(list) + len(list2)):
        if counter % 2 == 0:
            newlist.append(list[counter])
            counter += 1
        else:
            newlist.append(list2[counter])
            counter += 1
    return newlist

print(newlist(list, list2))

