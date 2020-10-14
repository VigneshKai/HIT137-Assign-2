import random
list = []
script = open('Exam Question 1.txt', 'r')
lines = script.readlines()
randNo = random.randint(0,2)
list = lines[randNo].split(', ')
print(list[0])
