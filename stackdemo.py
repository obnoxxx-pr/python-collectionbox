#!/usr/bin/env python3
from containerbox import Stack

s = Stack()

s.push(1)
s.push(2)
print("length:", len(s))
print("at top:", s.pop())
s.pop()
print("length after pop:", len(s))
print("new top:", s.peek())
