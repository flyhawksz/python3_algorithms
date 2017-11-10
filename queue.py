# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
#queue.py


class Queue:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        e = self.items.pop()
        return e

    def size(self):
        return len(self.items)
