from random import *
def oneTrial():
  flip1 = randint(0,1)==1
  flip2 = randint(0,1)==1
  flip3 = randint(0,1)==1
  numFlip = 3

  while not(flip1 == True and flip2 == True and flip3 == True):
    flip1 = flip2
    flip2 = flip3
    flip3 = randint(0,1)==1
    numFlip = numFlip + 1
  return numFlip

sum = 0
count = 0

#The more trails the more stable the results
#All the answers rounded to nearest integer is 14
while(count < 10000):
  sum = sum + oneTrial()
  count = count + 1

print(sum/count)