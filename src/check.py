def check(listAllMoves, attachedFields, kingPosition='51'):
    list1 = []
    list2 = []
    for i in attachedFields:
        list2.append(i[2:])

    for i in listAllMoves:
        if i[:2] == kingPosition:
            if i[2:] not in list2:
                list1.append(i)

    return list1

