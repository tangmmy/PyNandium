from typing import List
from gates.gates import AND,XOR,OR,ZERO16,NOT16,ONE,OR16,AND16,NOT

#Given a and b, return high bit(h) and low bit(l)
def HALF_ADDER(a:bool, b:bool):#(h: bool , l : bool)
    return [ AND(a,b) , XOR(a,b) ]


#Given a and b, return high bit(h) and low bit(l)
def FULL_ADDER(a:bool, b:bool,c:bool)->List[bool]:#(h: bool , l : bool)
    [h1,l1] = HALF_ADDER(a,b)
    [h2,l2] = HALF_ADDER(l1,c)
    return [ OR(h1,h2) , l2 ]

#if s = 0, b is selected, else a
def MUX(s:bool,a:bool,b:bool):
    a1 = AND(NOT(s),b)
    a2 = AND(s,a)
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


def INCREMENT(arr:List[bool]):
    res = _16BITS_ADDER(arr,ONE())
    return res


def _16BITS_MINUS(arr:List[bool],brr:List[bool]):
    return INCREMENT( _16BITS_ADDER(arr,NOT16(brr)))

def _16BITS_LESS_THAN_ZERO(arr:List[bool]):
    return arr[0]

def _16BITS_LESS_THAN_ZERO(arr:List[bool]):
    return arr[0]

def _16BITS_MUX(arr:List[bool],brr:List[bool],select:bool):
    res = []
    for i in range(16):
        res.append(MUX(select,arr[i],brr[i]))
    return res