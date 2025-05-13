from gates.gates import NAND

class SR_LATCH:
    def __init__(self):
        self.q = 1
        self.q_bar = 0

    def update(self,s,r):
        q_bar_next = NAND(s,self.q_bar)
        q_next = NAND(r,q_next)

        self.q=q_next
        self.q_bar = q_bar_next

    def output(self):
        return self.q

class D_LATCH:
    def __init__(self):
        self.q = 1
        self.q_bar = 0

    def update(self,s,r):
        q_bar_next = NAND(s,self.q_bar)
        q_next = NAND(r,q_next)

        self.q=q_next
        self.q_bar = q_bar_next

    def output(self):
        return self.q

class DATA_FLIP_FLOP:
    def __init__(self):
        pass



class _16BITS_REGISTER:
    def __init__(self):
        pass
    