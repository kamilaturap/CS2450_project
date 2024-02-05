def add(targetMemoryLocation, registersDictionary):
    num = int(registersDictionary[int(targetMemoryLocation)])
    return num

def divide(targetMemoryLocation, registersDictionary):
    num = int(registersDictionary[int(targetMemoryLocation)])
    return num

def branchneg(targetMemoryLocation, registersDictionary, accumulator):
    if accumulator < 0:
        return registersDictionary[int(targetMemoryLocation)]