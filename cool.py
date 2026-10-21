def alpaca(N, X):
    list = []
    failed = False
    for i in range(N):
        trynum = 1
        pastnum = 0 
        if i == 0:
            list.append(1)
            continue
        else:
            pastnum = list[i-1]
        currentX = 0
        while True:
            if (trynum + pastnum) % 2 == 0 and currentX != X:
                list.append(trynum)
                print(list)
                currentX += 1
                break
            elif (trynum + pastnum) % 2 != 0 and currentX == X:
                list.append(trynum)
                break
            elif trynum > 1000000000:
                failed = True
                break
    newlist = []
    if failed:
        print("-1")
    else:
        while len(list) > 0:
            newlist.append(list[len(list) - 1])
            list.remove(list[len(list) - 1])
    string = ""
    for i in newlist:
        if i + 1 == len(newlist):
            string += i
        else:
            string = string + str(i) + " "
    print(string)
alpaca(6, 4)
