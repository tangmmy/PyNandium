from typing import List
from gates.gates import AND,XOR,OR,ZERO16,NOT16,ONE,OR16,AND16,NOT,ONE16

#Given a and b, return high bit(h) and low bit(l)
def HALF_ADDER(a:bool, b:bool):#(h: bool , l : bool)
    return [ AND(a,b) , XOR(a,b) ]


#Given a and b, return high bit(h) and low bit(l)
def FULL_ADDER(a:bool, b:bool,c:bool)->List[bool]:#(h: bool , l : bool)
    [h1,l1] = HALF_ADDER(a,b)
    [h2,l2] = HALF_ADDER(l1,c)
    return [ OR(h1,h2) , l2 ]

#if s = 0, d0 is selected, else d1
def MUX(s:bool,d1:bool,d0:bool):
    a1 = AND(NOT(s),d0)
    a2 = AND(s,d1)
    return OR(a1,a2)




#note: starting from here, all numbers is in a form of [x0,x1,x2...,x15] , consisting of 16 elements, 
#                                                   x0 will be the least significant bit

def _16BITS_ADDER(arr:List[bool],brr:List[bool])->List[bool]:
    assert(len(arr)==16)
    assert(len(brr)==16)

    [carry,l] = HALF_ADDER(arr[0],brr[0])
    res = [l]

    for i in range(1,16):
        [h,l] = FULL_ADDER(arr[i],brr[i],carry)
        carry = h
        res = res + [l]

    return res


def INCREMENT(arr:List[bool])->List[bool]:
    res = _16BITS_ADDER(arr,ONE16())
    return res


def _16BITS_MINUS(arr:List[bool],brr:List[bool])->bool:
    return INCREMENT( _16BITS_ADDER(arr,NOT16(brr)))

def _16BITS_LESS_THAN_ZERO(arr:List[bool]):
    return arr[15]

def _16BITS_EQUAL_ZERO(arr:List[bool])->bool:
    for i in range(16):
        if(arr[i]==True):
            return True
    return False

def _16BITS_MUX(select:bool,d1:List[bool],d0:List[bool])->List[bool]:
    res = []
    for i in range(16):
        res.append(MUX(select,d1[i],d0[i]))
    return res