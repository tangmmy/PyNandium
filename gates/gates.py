from typing import List

#the ZERO,ONE and NAND will serve as the lowest abstraction hardware
def ZERO():
    return False
def ONE():
    return True
def NAND(a:bool, b:bool):
    if (a and b) :
       return False
    return True



def AND(a:bool, b:bool):  
    c = NAND(a,b)
    return NAND(c,c)

def NOT(a:bool):
    return NAND(a,a)

def OR(a:bool,b:bool):
    c = NAND(a,b)
    return NAND(NOT(a),NOT(b))

def XOR(a:bool, b:bool):
    c = NAND(a,b)
    d = NAND(a,c)
    e = NAND(c,b)
    return NAND(d,e)

def ZERO16():
    return [0]*16

def ONE16():
    return [1]+[0]*15

def NOT16(a: List[bool]):
    result = []
    for i in range(16):
        result.append(NOT(a[i]))
    return result


def AND16(a: List[bool],b: List[bool]):
    for i in range(16):
        a[i] = AND(a[i],b[i])
    return a


def OR16(a: List[bool],b: List[bool]):
    for i in range(16):
        a[i] = OR(a[i],b[i])
    return a

def XOR16(a: List[bool],b: List[bool]):
    for i in range(16):
        a[i] = XOR(a[i],b[i])
    return a
