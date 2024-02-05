def read(targetMemoryLocation, registersDictionary):
    word = input(f"enter signed four-digit word to be stored at {targetMemoryLocation}: ")
    registersDictionary[int(targetMemoryLocation)] = word
    return

def write(targetMemoryLocation, registersDictionary):
    print(registersDictionary[int(targetMemoryLocation)])
    return
