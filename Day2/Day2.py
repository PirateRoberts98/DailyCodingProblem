#!/usr/bin/env python


print("hello world")



default_input = [1,2,3,4,5]
output_array = [120,60,40,30,24]


def array_fix(arr):
    #assumption: All values passed are array with real numbers passed through
    product = 1
    ret = []
    for i in arr: #assumption: having a zero is okay
        product = product*i 
    for i in arr:
       ret.append(product/i) 
    return ret 

res = array_fix(default_input)

assert res == output_array 
