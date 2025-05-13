from typing import List

from circuits.circuits import _16BITS_MUX,_16BITS_ADDER,_16BITS_MINUS
from gates.gates import NOT16,AND16,OR16,XOR16,ONE16,ZERO16

def LOGIC_UNIT(op1:bool, op0:bool,X:List[bool],Y:List[bool]):
    d1 = _16BITS_MUX(op0,NOT16(X),XOR16(X,Y))
    d0 = _16BITS_MUX(op0,OR16(X,Y),AND16(X,Y))
    return _16BITS_MUX(op1,d1,d0)

def ARITHMETIC_UNIT(op1:bool, op0:bool,X:List[bool],Y:List[bool]):
    d0 = _16BITS_MUX(op0,_16BITS_ADDER(X,ONE16()),_16BITS_ADDER(X,Y))
    d1 = _16BITS_MUX(op0,_16BITS_MINUS(X,ONE16()),_16BITS_MINUS(X,Y))
    return _16BITS_MUX(d1,d0,op1)

def ALU(u:bool,op1:bool,op0:bool,zx:bool,sw:bool):
    X = _16BITS_MUX(zx,X,ZERO16(),_16BITS_MUX(Y,X,sw))
    Y = _16BITS_MUX(sw,X,Y)
    d1 = ARITHMETIC_UNIT(op1,op0,X,Y)
    d0 = LOGIC_UNIT(op1,op0,X,Y)
    return _16BITS_MUX(u,d1,d0)