# Problem Statement

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class
'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

The following test should pass:
'''
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

## Overview

This was a short 10 minute challenge. The goal was to attempt to see how to use recursion on this problem

### Description


##### Serialize
---
Serialize take the node and for each sub tree will add a ":" to sepeare and a ";" when the string of that tree (or sub tree) is done. 

Run Time: O(n) 
Run : O(n)