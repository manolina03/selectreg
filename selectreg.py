import random


sampleList = [x for x in range (0,32)]
print(sampleList)
 
randomList = random.choices(sampleList, weights=(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,5,5,5,5,5), k=3)
 
print(randomList) 
for i in randomList:
  regx="r"+str(i)
  print(regx)
