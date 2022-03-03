# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:55:28 2022

@author: manoi
"""

def countSubstrings(input_str):
    map_substr = {1:"ab", 2:"cde",3:"fgh", 4:"ijk", 5:"lmn", 6:"opq",7:"rst",8:"uvw",9:"xyz"}

    mapped = []
    divisible = 0 
    for i in range(0, len(input_str)):
        for k,v in map_substr.items():
            if input_str[i] in v:
                divisible+=1
                mapped.append(k)
    
    
    idx = 1
    len_map = len(mapped)
    while len_map:
        for j in range(0, len(mapped)-idx):
            list1 = mapped[j:j+idx+1]
            sum1 = sum(list1)
            if sum1 % len(list1) == 0:
                divisible+=1
        idx+=1
        len_map -=1
    return divisible

if __name__ == "__main__":
    input_str = input()
    result = countSubstrings(input_str)
    print(result)