testVal=116924417#13195#2147483646#13195
# 116924417 should be 11587 0x2d43
# 13195 should be 29
x=1

while x<testVal:
    x=x+1
    isPrime=1
    for y in range(2,x):
        if not x%y: #if x is divisible by y
            isPrime=0
            break
    if isPrime: #if isPrime is not zero
        if not testVal%x: #if testVal is divisible by x
			maxPrime=x 
			testVal=testVal/x #speeds up
			
print maxPrime

