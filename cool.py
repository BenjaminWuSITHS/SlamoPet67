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
    f_list = []
    looped = 0
    while works == False:
        addnum = 0
        f_list=[]
        currentX = 0
        for i in range(N):
            if i == 0:
                f_list.append(0+looped)
            while len(f_list) < X:
                if (f_list[i] + addnum) % 2 == 0 and (addnum) not in f_list:
                    print(f"{addnum} is not in {f_list}")
                    f_list.append(addnum)
                    addnum = 1
                    currentX += 1
                else:
                    addnum += 1
            while len(f_list) < N:
                if (f_list[i] + addnum) % 2 != 0 and (addnum) not in f_list:
                    print(f"{addnum} is not in {f_list}")
                    f_list.append(addnum)
                    addnum = 1
                    currentX += 1
                else:
                    addnum +=1
        checkHappy = 0
        checkSad = 0
        for i in range(len(f_list)):
            print(f"checking {f_list}")
            if i+1 == len(f_list):
                if (f_list[i] + f_list[0]) % 2 == 0:
                    checkHappy += 1
                else:
                    checkSad += 1
            elif (f_list[i] + f_list[i+1]) % 2 == 0:
                checkHappy += 1
                print(f"{f_list[i]}+{f_list[i+1]} is even")
            elif (f_list[i] + f_list[i+1]) % 2 != 0:
                checkSad += 1
                print(f"{f_list[i]}+{ f_list[i+1]} is odd")
        if checkHappy == X and checkSad == N-X:
            print(f_list)
            works = True
        else:
            print(f"doesnt work {checkHappy} doesnt equal {X}, {checkSad} doesnt equal {N-X}")
            looped += 1
            print(looped)

def alpaca(N, X): # stupid brute force which doesnt work
    if X > N or X < 0:
        return
    works = False
    f_list = []
    looped = 0
    while works == False:
        addnum = 0
        f_list=[]
        for i in range(N):
            if i == 0:
                f_list.append(0+looped)
            while len(f_list) < X:
                if (f_list[i] + addnum) % 2 == 0 and (addnum) not in f_list:
                    f_list.append(addnum)
                    addnum = 1
                else:
                    addnum += 1
                    if addnum > 100000:
                        print(-1)
                        return
            while len(f_list) < N:
                if (f_list[i] + addnum) % 2 != 0 and (addnum) not in f_list:
                    f_list.append(addnum)
                    addnum = 1
                else:
                    addnum +=1
                    if addnum > 100000:
                        print(-1)
                        return
        checkHappy = 0
        checkSad = 0
        for i in range(len(f_list)):
            if i+1 == len(f_list):
                if (f_list[i] + f_list[0]) % 2 == 0:
                    checkHappy += 1
                else:
                    checkSad += 1
            elif (f_list[i] + f_list[i+1]) % 2 == 0:
                checkHappy += 1
            elif (f_list[i] + f_list[i+1]) % 2 != 0:
                checkSad += 1
        if checkHappy == X and checkSad == N-X:
            print(f_list)
            works = True
        else:
            looped += 1

# 1 hour to figure out -->
# cannot have odd sad alpacas 
# [0,1,0] creates 2 sad alpacas and is made of 0+1 and 1+0 (which makes 2)
# ie [0,1,0,1] creates 4 sad alpacas
# and [0,1,0,0] creates 2 sad and 2 happy
# so that means 
def alpaca(N, X): #the genius solution at 4:38 AM
    sad = N - X

    if sad % 2 == 1:
        print(-1)
        return
    f_list = []
    for i in range(N):
        if i <= sad:
            f_list.append(i % 2)
        else:
            f_list.append(0)

    print(f_list)

alpaca(7,3)