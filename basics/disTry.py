import dis

def exampleFunction():
    a = 5
    b = 10
    result = a + b
    print(result)

dis.dis(exampleFunction)
