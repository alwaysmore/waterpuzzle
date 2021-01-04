import copy

sol = []

def findSolution(cups, start, end):
    if isEnd(cups):
        sol.append([start, end])
        return True
    else:
        length = len(cups)
        for i in range(length):
            if not isEmpty(cups[i]):
                dep, color, count = findTop(cups[i])
                #find a cup to pour in
                for i1 in range(length):
                    if i != i1:
                        if isEmpty(cups[i1]):
                            if dep + count != 4:
                                ti = copy.deepcopy(cups[i])
                                ti1 = copy.deepcopy(cups[i1])
                                res = False
                                #pour into it if it is empty
                                cups[i1] = [0] * (4 - count) + [color] *  count
                                cups[i][dep : dep + count] = [0] * count
                                res = findSolution(cups, i, i1)
                                if res:
                                    #if found then break all the loop
                                    sol.append([start, end])
                                    return True
                                else:
                                    #cancel the operation
                                    cups[i] = ti
                                    cups[i1] = ti1
                        else:
                            dep1, color1, count1 = findTop(cups[i1])
                            if color1 == color and dep1 >= count:
                                ti = copy.deepcopy(cups[i])
                                ti1 = copy.deepcopy(cups[i1])
                                res = False
                                #pour into if it is enough to hold it
                                cups[i][dep : dep + count] = [0] * count
                                cups[i1][dep1 - count : dep1] = [color] * count
                                res = findSolution(cups, i, i1)
                                if res:
                                    #if found then break all the loop
                                    sol.append([start, end])
                                    return True
                                else:
                                    #cancel the operation
                                    cups[i] = ti
                                    cups[i1] = ti1
    #print('cancel' + str([start, end]))
    return False

def isEmpty(cup):
    if cup == [0] * 4:
        return True
    return False

def findTop(cup):
    #print('Find Top:' + str(cup))
    index = 0
    while(cup[index] == 0):
        index += 1
    retTop = index
    retColor = cup[index]
    retCount = 0
    for i in range(index,4,1):
        if cup[i] == retColor:
            retCount += 1
        else:
            break
    return retTop, retColor, retCount

def isEnd(cups):
    for c in cups:
        if c.count(c[0]) != 4:
            return False
    return True

if __name__ == '__main__':
    #print('Hello World!')
    cups = []
    #n_cup = int(input('Enter the number of cups:'))
    n_cup = 14
    # cups = [
    #     [1,2,3,4],
    #     [2,3,5,1],
    #     [6,7,1,6],
    #     [7,4,5,7],
    #     [6,3,4,5],
    #     [1,2,2,7],
    #     [3,4,6,5],
    #     [0,0,0,0],
    #     [0,0,0,0]
    # ]
    cups =[
        [1,2,3,3],
        [4,5,6,7],
        [8,4,9,10],
        [8,5,9,8],
        [2,9,11,1],
        [11,2,10,2],
        [10,4,9,12],
        [12,4,5,12],
        [6,7,3,1],
        [10,11,7,6],
        [7,11,12,1],
        [6,3,5,8],
        [0,0,0,0],
        [0,0,0,0]
    ]

    print('Solving ...')
    findSolution(cups, -1, -1)
    #print(findSolution(cups, -1, -1))
    #print(cups)
    sol.pop()
    sol.reverse()
    for i in sol:
        print('%2d -> %2d' %(i[0] + 1, i[1] + 1))
