import matrixGen

testDict = matrixGen.generateDict() 

print('------------------testDict-----------------------')
print(testDict)
print('-----------------------------------------')

def decryptDict(woerterbuch):
 decryptionDict = {}  
 for key in woerterbuch:
  decryptionDict[woerterbuch[key]] = key
 return decryptionDict


print('------------------decryptDict-----------------------')
print(decryptDict(testDict))
print('-----------------------------------------')