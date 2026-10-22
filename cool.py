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

def alpaca(N, X):
    works = False
    list = []
    looped = 0
    while works == False:
        nextnum = 0
        currnum = (1+looped)
        print(currnum)
        currentX = 0
        while currentX < X:
            if (currnum + nextnum) % 2 != 0 or nextnum in list:
                nextnum += 1
            elif (currnum + nextnum) % 2 == 0 and nextnum not in list:
                list.append(nextnum)
                currnum = nextnum
                currentX += 1
                if len(list) == X:
                    while currentX <= N-1:
                        if (currnum + nextnum) % 2 != 0 and nextnum not in list:
                            list.append(nextnum)
                            currnum = nextnum
                            currentX += 1
                        elif (currnum + nextnum) % 2 == 0:
                            nextnum +=1
            elif nextnum == 1000000000:
                print(-1)
                return
        checkHappy = 0
        checkSad = 0
        for i in range(len(list)):
            print(f"checking {list}")
            if i+1 == len(list):
                if list[i] + list[0] % 2 == 0:
                    checkHappy += 1
                else:
                    checkSad += 1
            elif list[i] + list[i+1] % 2 == 0:
                checkHappy += 1
                print(f"{list[i]}+{list[i+1]} is even")
            elif list[i] + list[i+1] % 2 != 0:
                checkSad += 1
                print(f"{list[i]}+{ list[i+1]} is odd")
        if checkHappy == X and checkSad == N-X:
            print(list)
            works = True
        else:
            print(f"doesnt work {checkHappy} doesnt equal {X}, {checkSad} doesnt equal {N-X}")
            list=[]
            looped += 1
            print(looped)
alpaca(6,4)