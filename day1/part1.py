import os

values=[]


def evalstring(line):
    for charval1 in line:
        if charval1.isnumeric():
            # print(charval1)
            break
    for charval2 in line[::-1]:
        if charval2.isnumeric():
            # print(charval2)
            break
    return charval1,charval2


def mknum(chars):
    num = chars[0]+chars[1]
    return(int(num))
    
def appendvalue(num):
    values.append(num)
    
# print(mknum(evalstring('h3ll0')))

def sumvalues(list):
    total = 0
    for listval in list:
        total += listval
    return total


path = '/home/advent/aoc2023/day1/'
os.listdir(path)
file = open('input.txt', 'r')

for line in file.readlines():
    valset=evalstring(line)
    print(valset)
    valnum=mknum(valset)
    print(valnum)
    appendvalue(valnum)
    
file.close()

print(values)
print(sumvalues(values))