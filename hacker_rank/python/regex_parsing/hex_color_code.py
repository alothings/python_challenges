"""
#####################################################################
Intro:

Task:

Input:

Output:

"""

import re

if __name__ == '__main__':
    for i in range(int(input())):
        # matches = re.findall(r':?.(#[0-9a-fA-F]{3,6})', input())
        matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
        if matches:
            print(*matches, sep='\n')

""" Test input:
    11
    #BED
    {
        color: #FfFdF8; background-color:#aef;
        font-size: 123px;
        background: -webkit-linear-gradient(top, #f9f9f9, #fff);
    }
    #Cab
    {
        background-color: #ABCC;
        border: 2px dashed #ffff;
    }   

"""