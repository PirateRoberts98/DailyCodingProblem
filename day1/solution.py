

# x: list , k: integer
def check_summed_pair(list,k):
    paired = dict()
    for i in list:
        if k-i in paired:
            return True
        else:
            paired[i] = True
    return False

assert check_summed_pair([10, 15, 3, 7]  , 17) == True
assert check_summed_pair([0, 17, 3, 7]  , 17) == True
assert check_summed_pair([0, 16, 3, 7]  , 17) == False