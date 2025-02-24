'''''''''''''''''''''''''''Task 1'''''''''''''''''''''''''''
import math
math.prod([1, 2, 3, 4, 5, 6])

'''''''''''''''''''''''''''Task 2'''''''''''''''''''''''''''
b = str(input())
countu = 0
countl = 0
for i in b:
    if i.isupper():
        countu+=1
    elif i.islower():
        countl+=1
print(countu,countl)

'''''''''''''''''''''''''''Task 3'''''''''''''''''''''''''''
s = str(input())
k = ''.join(reversed(s))
if s == k:
    print('Yes')
else:
    print('No')

'''''''''''''''''''''''''''Task 4'''''''''''''''''''''''''''
import time
a = int(input())
d = int(input())
time.sleep(d/1000)
print(math.sqrt(a))

'''''''''''''''''''''''''''Task 5'''''''''''''''''''''''''''
da = (True,False,True,True)
print(all(da))