#-*- coding: utf-8 -*-
def FastPower(a,b) :
    if b == 1:
        return a
    else:
        c = a*a
        ans = FastPower(c,b/2)

    if b % 2 != 0:
        return a*ans
    else:
        return ans

if __name__ == "__main__":
    print FastPower(2, 9)