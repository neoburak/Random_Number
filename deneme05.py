import random

list = []

while (len(list)>=0):
    list.append(random.randint(0,9))
    if(len(list)>=5):
        break


print(list)