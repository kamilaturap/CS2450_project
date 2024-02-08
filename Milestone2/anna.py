def add(targetMemoryLocation, registersDictionary):
    num = int(registersDictionary[int(targetMemoryLocation)])
    return num

def divide(targetMemoryLocation, registersDictionary):
    num = int(registersDictionary[int(targetMemoryLocation)])
    return num

def branchneg(targetMemoryLocation, accumulator, current_index):

    if(accumulator < 0):
        return int(targetMemoryLocation) - 1
    else:
        return current_index
    
