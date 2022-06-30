#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr,n):
    # Write your code here
    contMenor = 0
    contMaior = 0 
    contZero = 0
    for i in arr:
        if i < 0:
            contMenor+=1
            
        elif i > 0:
            contMaior +=1
           
        elif i == 0:
            contZero +=1
            
    positive = contMaior/n
    negative = contMenor/n
    zeros = contZero/n
    print('%.6f'% positive)
    print('%.6f'% negative)
    print('%.6f'% zeros)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr,n)