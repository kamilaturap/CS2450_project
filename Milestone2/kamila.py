def subtract(targetMemoryLocation, registersDictionary, accumulator):
    num = int(registersDictionary[int(targetMemoryLocation)])
    return accumulator - num


def multiply(targetMemoryLocation, registersDictionary, accumulator):
    num = int(registersDictionary[int(targetMemoryLocation)])
    return accumulator * num


def branchzero(targetMemoryLocation, accumulator, current_index):
    if accumulator == 0:
        return int(targetMemoryLocation) - 1
    else:
        return current_index
