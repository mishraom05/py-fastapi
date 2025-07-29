import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Imports.average as IA
import Imports.sum as IS

def calculate(fnum, snum, tnum):
    print(f"Sum is {IS.calc_sum(fnum=fnum, snum=snum, tnum=tnum)}")
    print(f"Average is {IA.calc_avg(fnum=fnum, snum=snum, tnum=tnum)}")

if __name__ == '__main__':
    fnum=float(input("Enter first number:"))
    snum=float(input("Enter second number:"))
    tnum=float(input("Enter third number:"))
    calculate(fnum=fnum, snum=snum, tnum=tnum)