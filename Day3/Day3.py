#!/usr/bin/env python

#Day 3 Code



class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#----------------------------------------------------------------------------------------------------------------------------------------


def serialize(node): #assumption: Node.value does is itself has a toString and does not include : or ; 
    if node == None or node.val == None:
        return ""
    else:
        return str(node.val) + ":" +serialize(node.left) + ":" + serialize(node.right) + ";"

def deserialize(string):
    if (not isinstance(string,str)):
        raise Exception
    pass
    return Node(None,None,None)

#----------------------------------------------------------------------------------------------------------------------------------------

def mainTest():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(node))
    assert deserialize(serialize(node)).left.left.val == 'left.left'

def functionTest(): #Helper class for developing to ensure parameter passed is correct 
    serialize(Node("a",None,None))
    deserialize("")
#----------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    functionTest()
    mainTest()